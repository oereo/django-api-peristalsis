from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User

from accounts.managers import UserDefaultManager
from django.db.models.signals import post_save


# class User(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email',
#         max_length=255,
#         unique=True,
#     )
#     user_created = models.DateTimeField(auto_now_add=True, help_text="유저 생성 시점")
#     last_login = models.DateTimeField(auto_now=True, help_text="유저의 마지막 로그인 logging")
#     withdrew_at = models.DateTimeField(blank=True, null=True, verbose_name='탈퇴 시점')
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     name = models.CharField(max_length=31)
#     birth_day = models.CharField(max_length=32, blank=True, help_text='생년월일')  # birth_day
#     phone_number = models.CharField(max_length=14, unique=True)
#     is_removed = models.BooleanField(default=False)
#
#     objects = UserDefaultManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'phone_number', 'birth_day']
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#
#     @property
#     def is_staff(self):
#         return self.is_admin
#
#     @property
#     def following_count(self):
#         return User.objects.filter(followed=self).count()
#
#     @property
#     def followed_count(self):
#         return User.objects.filter(following=self).count()
#

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_pk = models.IntegerField(blank=True)
    email = models.EmailField(max_length=500, blank=True)
    mygit = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to="profile/image", default='red.jpg')
    myInfo = models.CharField(max_length=150, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

