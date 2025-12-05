from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("events/", views.events, name="events"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("feedback/", views.feedback, name="feedback"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
    path("events/<int:event_id>/register/", views.register_for_event, name="register_for_event"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("settings/", views.settings_view, name="settings"),
    path("profile/cancel-registration/<int:registration_id>/", views.cancel_registration, name="cancel_registration"),
    path("events/<int:event_id>/participants/", views.event_participants_view, name="event_participants"),
    path("events/participants/remove/<int:registration_id>/", views.remove_participant, name="remove_participant"),
    path("profile/create-event/", views.create_event_view, name="create_event"),
    path("profile/assign-curator/", views.assign_curator, name="assign_curator"),
    path("profile/delete-user/", views.delete_user, name="delete_user"),
    path("profile/export-excel/", views.export_conferences_excel, name="export_excel"),
    path("profile/message/<int:message_id>/update-status/", views.update_message_status, name="update_message_status"),
    path("profile/message/<int:message_id>/delete/", views.delete_message, name="delete_message"),
]
