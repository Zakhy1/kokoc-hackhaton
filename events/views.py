from django.shortcuts import render

from events.models import Event


def index(request):
    return render(request, "events/index.html")


def activities(request):
    events = Event.objects.all()
    return render(request, "events/activities.html", {"events": events})
