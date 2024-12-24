from django.urls import path
from events.views import admin_views, user_views

urlpatterns = [
    # Admin URLs
    path('admin/events/', admin_views.admin_event_list, name='admin_event_list'),
    path('admin/events/create/', admin_views.admin_event_create, name='admin_event_create'),
    path('admin/events/delete/<int:event_id>/', admin_views.admin_event_delete, name='admin_event_delete'),

    # User URLs
    path('', user_views.event_list, name='event_list'),
    path('events/<int:event_id>/', user_views.event_detail, name='event_detail'),
    path('events/<int:event_id>/purchase/', user_views.ticket_purchase, name='ticket_purchase'),
    path('events/<int:event_id>/feedback/', user_views.event_feedback, name='event_feedback'),
    path('notifications/', user_views.user_notifications, name='user_notifications'),
]
