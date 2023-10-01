from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from events.forms import EventConfirmForm
from events.models import Event, EventProof
from organisations.models import Fund


def index(request):
    funds = Fund.objects.all()
    return render(request, "events/index.html", {"funds": funds})


@login_required
def activities(request):
    user = request.user
    actual_events = user.events.values_list("pk", flat=True)
    done_events = user.events_done.values_list('pk', flat=True)
    events = Event.objects.filter(user=user).exclude(pk__in=done_events).exclude(pk__in=actual_events)
    return render(request, "events/activities.html", {"events": events})


@login_required
def participate(request, event_id):
    user = request.user
    event = Event.objects.get(id=event_id)
    user.events.add(event)
    return redirect("users:profile")


@login_required
def confirm_event(request, event_id):
    if request.method == "POST":
        form = EventConfirmForm(files=request.FILES)
        if form.is_valid():
            proof_obj = form.save(commit=False)
            proof_obj.user = request.user
            proof_obj.event = Event.objects.get(id=event_id)
            proof_obj.save()
            messages.success(request, "Подтверждение добавлено")
            return redirect("users:profile")
    form = EventConfirmForm()
    return render(request, "events/proof.html", {"form": form})
