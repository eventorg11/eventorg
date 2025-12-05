from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError
from app.models import Conference, EventRegistration
from app.forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ProfileUpdateForm,
    ConferenceCreationForm,
)


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
    user_profile = getattr(request.user, 'profile', None)
    is_curator = user_profile and user_profile.is_curator()
    
    if is_curator:
        curated_conferences = Conference.objects.filter(
            curator=request.user
        ).order_by('-created_at')
        
        for conference in curated_conferences:
            conference.registration_count = EventRegistration.objects.filter(
                conference=conference
            ).count()
        
        context = {
            'is_curator': True,
            'curated_conferences': curated_conferences,
        }
    else:
        registrations = EventRegistration.objects.filter(
            user=request.user
        ).select_related('conference').order_by('-created_at')
        context = {
            'is_curator': False,
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


@login_required
def settings_view(request):
    """Страница настроек пользователя"""
    from django.contrib.auth.forms import PasswordChangeForm

    profile_success = False
    password_success = False

    profile_form = ProfileUpdateForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)
    for field in password_form.fields.values():
        field.widget.attrs.update({"class": "form-control"})

    if request.method == 'POST':
        if 'profile_submit' in request.POST:
            profile_form = ProfileUpdateForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                profile_success = True
            password_form = PasswordChangeForm(user=request.user)
            for field in password_form.fields.values():
                field.widget.attrs.update({"class": "form-control"})
        elif 'password_submit' in request.POST:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            profile_form = ProfileUpdateForm(instance=request.user)
            for field in password_form.fields.values():
                field.widget.attrs.update({"class": "form-control"})
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                password_success = True

    context = {
        'profile_form': profile_form,
        'password_form': password_form,
        'profile_success': profile_success,
        'password_success': password_success,
    }
    return render(request, 'settings.html', context)


@login_required
def event_participants_view(request, event_id):
    """Страница со списком зарегистрированных пользователей на мероприятие"""
    conference = get_object_or_404(Conference, id=event_id)
    
    user_profile = getattr(request.user, 'profile', None)
    is_curator = user_profile and user_profile.is_curator()
    is_admin = user_profile and user_profile.is_admin()
    
    if not (is_curator and conference.curator == request.user) and not is_admin:
        return redirect('profile')
    
    registrations = EventRegistration.objects.filter(
        conference=conference
    ).select_related('user').order_by('-created_at')
    
    context = {
        'conference': conference,
        'registrations': registrations,
        'registration_count': registrations.count(),
        'max_participants': conference.max_participants,
    }
    
    return render(request, 'event_participants.html', context)


@login_required
def remove_participant(request, registration_id):
    """Удаление регистрации участника (для куратора)"""
    registration = get_object_or_404(EventRegistration, id=registration_id)
    conference = registration.conference
    
    user_profile = getattr(request.user, 'profile', None)
    is_curator = user_profile and user_profile.is_curator()
    is_admin = user_profile and user_profile.is_admin()
    
    if not (is_curator and conference.curator == request.user) and not is_admin:
        return JsonResponse({'success': False, 'error': 'Нет доступа'}, status=403)
    
    if request.method == 'POST':
        user_name = f"{registration.user.first_name} {registration.user.last_name}".strip() or registration.user.username
        registration.delete()
        return JsonResponse({
            'success': True,
            'message': f'Регистрация пользователя {user_name} успешно удалена'
        })
    
    return JsonResponse({'success': False, 'error': 'Неверный метод запроса'}, status=400)


@login_required
def create_event_view(request):
    """Страница создания мероприятия для куратора"""
    user_profile = getattr(request.user, 'profile', None)
    is_curator = user_profile and user_profile.is_curator()
    is_admin = user_profile and user_profile.is_admin()
    
    if not is_curator and not is_admin:
        return redirect('profile')
    
    if request.method == 'POST':
        form = ConferenceCreationForm(request.POST)
        if form.is_valid():
            conference = form.save(commit=False)
            conference.curator = request.user
            conference.status = 'not_started'
            conference.save()
            return redirect('profile')
    else:
        form = ConferenceCreationForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'create_event.html', context)
