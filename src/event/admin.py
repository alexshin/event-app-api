from django.contrib import admin
from .models import Category, Event, Organizer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    pass
