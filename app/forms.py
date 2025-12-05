from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from app.models import Conference

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """Форма регистрации пользователя"""

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )

    first_name = forms.CharField(
        required=True,
        label="Имя",
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите имя"}
        ),
    )

    last_name = forms.CharField(
        required=True,
        label="Фамилия",
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите фамилию"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите имя пользователя",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Подтвердите пароль"}
        )


class CustomAuthenticationForm(AuthenticationForm):
    """Форма входа пользователя"""

    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите имя пользователя",
                "autofocus": True,
            }
        ),
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Введите пароль"}
        ),
    )


class ProfileUpdateForm(forms.ModelForm):
    """Форма обновления профиля пользователя"""

    first_name = forms.CharField(
        required=False,
        label="Имя",
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите имя"}
        ),
    )

    last_name = forms.CharField(
        required=False,
        label="Фамилия",
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите фамилию"}
        ),
    )

    email = forms.EmailField(
        required=False,
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ConferenceCreationForm(forms.ModelForm):
    """Форма создания мероприятия для куратора"""
    
    class Meta:
        model = Conference
        fields = [
            'title',
            'short_description',
            'description',
            'start_date',
            'is_online',
            'location',
            'online_link',
            'registration_deadline',
            'max_participants',
            'organizer_name',
            'contact_email',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название мероприятия'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание (до 500 символов)',
                'rows': 3
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Подробное описание мероприятия',
                'rows': 6
            }),
            'start_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'is_online': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес или место проведения'
            }),
            'online_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/meeting'
            }),
            'registration_deadline': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'max_participants': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Максимальное количество участников',
                'min': 1
            }),
            'organizer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название организации-организатора'
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com'
            }),
        }
        labels = {
            'title': 'Название мероприятия',
            'short_description': 'Краткое описание',
            'description': 'Описание',
            'start_date': 'Дата и время начала',
            'is_online': 'Онлайн мероприятие',
            'location': 'Место проведения',
            'online_link': 'Ссылка для онлайн участия',
            'registration_deadline': 'Срок регистрации',
            'max_participants': 'Максимальное количество участников',
            'organizer_name': 'Организатор',
            'contact_email': 'Контактный email',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['description'].required = True
        self.fields['start_date'].required = True
        self.fields['location'].required = False
        self.fields['online_link'].required = False


class ContactForm(forms.Form):
    """Форма обратной связи"""
    
    name = forms.CharField(
        required=True,
        label="Имя",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя"
            }
        ),
    )
    
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email"
            }
        ),
    )
    
    subject = forms.CharField(
        required=True,
        label="Тема",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Тема сообщения"
            }
        ),
    )
    
    message = forms.CharField(
        required=True,
        label="Сообщение",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше сообщение",
                "rows": 6
            }
        ),
    )
