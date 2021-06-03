from django.contrib import admin

# Register your models here.
from .models import User, ZooEvent, EventsHaveUsers

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_surname', 'user_email')
    list_filter = ('user_name', 'user_email')


class ZooEventAdmin(admin.ModelAdmin):
    list_display = ['event_name']


class EventsHaveUsersAdmin(admin.ModelAdmin):
    list_display = ['user', 'tickets_count']


admin.site.register(User, UserAdmin)
admin.site.register(ZooEvent, ZooEventAdmin)
admin.site.register(EventsHaveUsers, EventsHaveUsersAdmin)
