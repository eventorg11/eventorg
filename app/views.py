from django.shortcuts import render
from app.models import Conference


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def events(request):
    """Страница со списком всех мероприятий"""
    conferences = Conference.objects.all().order_by("-start_date")
    return render(request, "events.html", {"conferences": conferences})
