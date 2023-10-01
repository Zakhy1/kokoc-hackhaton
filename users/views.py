from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from events.models import EventProof
from users.forms import UserRegistrationForm, UserEditForm


def register_user(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return redirect("users:login")

    user_form = UserRegistrationForm()
    return render(request, "users/register.html",
                  {"user_form": user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Профиль обновлен")
        else:
            messages.error(request, "Ошибка при обновлении профиля")
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, "users/edit.html",
                  {"user_form": user_form})


@login_required
def profile(request):
    user = request.user
    events_active = user.events.all()
    events_done = user.events_done.all()
    return render(request, "users/profile.html",
                  {"user": user, "events_active": events_active, "events_done": events_done})
