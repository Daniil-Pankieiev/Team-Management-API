from django.contrib import admin
from .models import Team
from members.models import Person


class PersonInline(admin.TabularInline):
    model = Person
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    inlines = [PersonInline]
