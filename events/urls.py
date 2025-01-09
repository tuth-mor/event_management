from django.urls import path
from events.views import (
    register_user,
    login_user,
    logout_user,
    event_register,
    event_list,
    event_detail,
    ticket_purchase,
    event_feedback,
    user_notifications,
)

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('events/register/', event_register, name='event_register'),
    path('', event_list, name='event_list'),
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('<int:event_id>/purchase/', ticket_purchase, name='ticket_purchase'),
    path('<int:event_id>/feedback/', event_feedback, name='event_feedback'),
    path('notifications/', user_notifications, name='user_notifications'),
]
