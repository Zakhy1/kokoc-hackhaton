from django.shortcuts import render

from events.models import Event


def index(request):
    return render(request, "events/index.html", {"events": events})
