from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """Профиль пользователя с ролью"""
    
    ROLE_CHOICES = [
        ('student', 'Студент'),
        ('curator', 'Куратор'),
        ('admin', 'Администратор'),
    ]
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь'
    )
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student',
        verbose_name='Роль',
        help_text='Роль пользователя в системе'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        indexes = [
            models.Index(fields=['role']),
        ]
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
    def is_student(self):
        """Проверяет, является ли пользователь студентом"""
        return self.role == 'student'
    
    def is_curator(self):
        """Проверяет, является ли пользователь куратором"""
        return self.role == 'curator'
    
    def is_admin(self):
        """Проверяет, является ли пользователь администратором"""
        return self.role == 'admin'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """Автоматически создает профиль при создании пользователя"""
    if created:
        UserProfile.objects.get_or_create(user=instance, defaults={'role': 'student'})


class Conference(models.Model):
    """Модель для конференций/мероприятий"""
    
    STATUS_CHOICES = [
        ('not_started', 'Не началась'),
        ('completed', 'Завершена'),
    ]
    
    title = models.CharField(
        max_length=200,
        verbose_name='Название конференции',
        help_text='Полное название конференции или мероприятия'
    )
    
    description = models.TextField(
        verbose_name='Описание',
        help_text='Подробное описание конференции'
    )
    
    short_description = models.CharField(
        max_length=500,
        blank=True,
        verbose_name='Краткое описание',
        help_text='Краткое описание для карточек и списков'
    )
    
    start_date = models.DateTimeField(
        verbose_name='Дата начала',
        help_text='Дата и время начала конференции'
    )
    
    location = models.CharField(
        max_length=200,
        verbose_name='Место проведения',
        help_text='Адрес или место проведения конференции'
    )
    
    is_online = models.BooleanField(
        default=False,
        verbose_name='Онлайн мероприятие',
        help_text='Отметьте, если конференция проводится онлайн'
    )
    
    online_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка для онлайн участия',
        help_text='Ссылка для подключения к онлайн конференции'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not_started',
        verbose_name='Статус',
        help_text='Текущий статус конференции'
    )
    
    registration_deadline = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Срок регистрации',
        help_text='Последний срок для регистрации участников'
    )
    
    max_participants = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Максимальное количество участников',
        help_text='Максимальное количество участников (если ограничено)'
    )
    
    organizer_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Организатор',
        help_text='Название организации-организатора'
    )
    
    contact_email = models.EmailField(
        blank=True,
        verbose_name='Контактный email',
        help_text='Email для связи с организаторами'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    curator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Куратор',
        help_text='Пользователь-куратор, создавший данное мероприятие',
        related_name='curated_conferences'
    )
    
    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['start_date']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return self.title
    
    @property
    def is_registration_open(self):
        """Проверяет, открыта ли регистрация"""
        if self.status != 'not_started':
            return False
        
        if not self.registration_deadline:
            return True
        
        now = timezone.now()
        deadline = self.registration_deadline
        
        if timezone.is_naive(deadline):
            default_tz = timezone.get_current_timezone()
            deadline = timezone.make_aware(deadline, default_tz)
        elif timezone.is_aware(deadline):
            deadline = timezone.localtime(deadline)
        
        return now <= deadline
    
    def is_upcoming(self):
        """Проверяет, является ли конференция предстоящей"""
        return self.start_date > timezone.now() and self.status == 'not_started'
    
    def is_past(self):
        """Проверяет, является ли конференция прошедшей"""
        return self.status == 'completed'


class EventRegistration(models.Model):
    """Модель для регистрации пользователей на мероприятия"""
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='event_registrations'
    )
    
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        verbose_name='Конференция',
        related_name='registrations'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    class Meta:
        verbose_name = 'Регистрация на мероприятие'
        verbose_name_plural = 'Регистрации на мероприятия'
        unique_together = ['user', 'conference']
        indexes = [
            models.Index(fields=['user', 'conference']),
            models.Index(fields=['conference']),
        ]
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.conference.title}"

