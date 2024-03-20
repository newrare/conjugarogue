from django.contrib import admin
from .models import Player



@admin.register(Player)
class AuthorAdmin(admin.ModelAdmin):
    pass
