from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


# admin.site.register(User)
admin.site.register(Profile)
