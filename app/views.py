from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError
from app.models import Conference, EventRegistration
from app.forms import CustomUserCreationForm, CustomAuthenticationForm


def index(request):
    """Главная страница с ближайшими мероприятиями"""
    now = timezone.now()
    
    upcoming_conferences = Conference.objects.filter(
        start_date__gte=now
    ).order_by('start_date')[:2]
    
    if upcoming_conferences.count() < 2:
        additional_needed = 2 - upcoming_conferences.count()
        additional = Conference.objects.filter(
            start_date__lt=now
        ).order_by('-start_date')[:additional_needed]
        upcoming_conferences = list(upcoming_conferences) + list(additional)
    
    return render(request, "index.html", {"upcoming_conferences": upcoming_conferences})


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
    is_registered = False
    if request.user.is_authenticated:
        is_registered = EventRegistration.objects.filter(
            user=request.user,
            conference=conference
        ).exists()
    
    context = {
        'conference': conference,
        'is_registered': is_registered,
    }
    return render(request, "event_detail.html", context)


@login_required
def register_for_event(request, event_id):
    """Регистрация пользователя на мероприятие"""
    conference = get_object_or_404(Conference, id=event_id)
    
    if request.method == 'POST':
        if not conference.is_registration_open:
            return JsonResponse({'success': False, 'error': 'Регистрация на это мероприятие закрыта'}, status=400)
        
        if conference.max_participants:
            current_registrations = EventRegistration.objects.filter(conference=conference).count()
            if current_registrations >= conference.max_participants:
                return JsonResponse({'success': False, 'error': 'Достигнуто максимальное количество участников'}, status=400)
        
        try:
            EventRegistration.objects.create(user=request.user, conference=conference)
            return JsonResponse({'success': True, 'message': 'Вы успешно зарегистрированы на мероприятие'})
        except IntegrityError:
            return JsonResponse({'success': False, 'error': 'Вы уже зарегистрированы на это мероприятие'}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Неверный метод запроса'}, status=405)


def register_view(request):
    """Страница регистрации"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    """Страница входа"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})


@login_required
def logout_view(request):
    """Выход из системы"""
    logout(request)
    return redirect('index')


@login_required
def profile_view(request):
    """Страница личного кабинета пользователя"""
    registrations = EventRegistration.objects.filter(
        user=request.user
    ).select_related('conference').order_by('-created_at')
    
    context = {
        'registrations': registrations,
    }
    return render(request, 'profile.html', context)


@login_required
def cancel_registration(request, registration_id):
    """Отмена регистрации пользователя на мероприятие"""
    registration = get_object_or_404(
        EventRegistration,
        id=registration_id,
        user=request.user
    )
    
    if request.method == 'POST':
        conference_title = registration.conference.title
        registration.delete()
        return JsonResponse({
            'success': True,
            'message': f'Регистрация на мероприятие "{conference_title}" отменена'
        })
    
    return JsonResponse({'success': False, 'error': 'Неверный метод запроса'}, status=405)
