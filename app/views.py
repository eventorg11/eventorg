from django.shortcuts import render, get_object_or_404
from app.models import Conference


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def events(request):
    """Страница со списком всех мероприятий"""
    conferences = Conference.objects.all().order_by("-start_date")
    return render(request, "events.html", {"conferences": conferences})


def contact(request):
    """Страница контактов"""
    return render(request, "contact.html")


def event_detail(request, event_id):
    """Детализированная страница просмотра мероприятия"""
    conference = get_object_or_404(Conference, id=event_id)
    return render(request, "event_detail.html", {"conference": conference})
