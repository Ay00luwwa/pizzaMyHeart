from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'role', 'is_active', 'created_at')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'facebook_profile', 'instagram_profile', 'twitter_profile')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'role')}),
    )
