from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from organisations.forms import FundRegisterForm, OrganisationRegisterForm


@login_required
def register_fund(request):
    user = request.user
    if request.method == "POST":
        form = FundRegisterForm(data=request.POST)
        if form.is_valid():
            new_fund = form.save(commit=False)
            new_fund.owner = user
            new_fund.save()
            messages.success(request, "Фонд зарегистрирован")
            return render(request, "events/reg_fund.html", {"form": form})
            # return redirect(new_fund.get_absolute_url())
    else:
        form = FundRegisterForm()
        return render(request, "events/reg_fund.html", {"form": form})


def register_organisation(request):
    user = request.user
    if request.method == "POST":
        form = OrganisationRegisterForm(request.POST)
        if form.is_valid():
            new_org = form.save(commit=False)
            new_org.owner = user
            new_org.save()
            messages.success(request, "Организация зарегистрирована")
            return render(request, "events/reg_org.html", {"form": form})
    else:
        form = OrganisationRegisterForm()
        return render(request, "events/reg_org.html", {"form": form})
