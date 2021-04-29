from django.contrib import admin

from .models import Profile, User


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


admin.site.register(User)
admin.site.register(Profile)
