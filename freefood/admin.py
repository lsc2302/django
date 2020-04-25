from django.contrib import admin
# Register your models here.

from .models import Event, User


class EventAdmin(admin.ModelAdmin):
    list_display = ["Etitle", "Etype", "Estart", "Eend", "Eopen", "Eplace", "Edescription", "Ersvps"]
    search_fields = ['Etitle']
    list_per_page = 10


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "location", "email", "tel"]
    search_fields = ['username']
    list_per_page = 10


admin.site.register(Event, EventAdmin)
admin.site.register(User, UserAdmin)
