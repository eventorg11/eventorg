from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("events/", views.events, name="events"),
    path("contact/", views.contact, name="contact"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
