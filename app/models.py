from django.db import models
from django.utils import timezone
from django.conf import settings


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
    
    def is_registration_open(self):
        """Проверяет, открыта ли регистрация"""
        if not self.registration_deadline:
            return self.status == 'not_started'
        return (
            self.status == 'not_started' and 
            timezone.now() <= self.registration_deadline
        )
    
    def is_upcoming(self):
        """Проверяет, является ли конференция предстоящей"""
        return self.start_date > timezone.now() and self.status == 'not_started'
    
    def is_past(self):
        """Проверяет, является ли конференция прошедшей"""
        return self.status == 'completed'

