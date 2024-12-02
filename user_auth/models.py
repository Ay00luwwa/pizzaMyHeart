from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=255, choices=[
        ('admin', 'Admin'),
        ('user', 'User'),
        # Add more roles as needed
    ])
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    facebook_profile = models.URLField(blank=True, null=True)
    instagram_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True
    )

    def __str__(self):
        return self.username

    def delete(self, using=None, keep_parents=False):
        self.is_active = False 
        self.save(using=using)
