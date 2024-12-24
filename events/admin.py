from django.contrib import admin
from .models import User, Event, Category, Ticket, Feedback, Sponsor, Notification

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Ticket)
admin.site.register(Feedback)
admin.site.register(Sponsor)
admin.site.register(Notification)