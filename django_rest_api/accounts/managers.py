from django.contrib.auth.base_user import BaseUserManager


class UserDefaultManager(BaseUserManager):
    def create_user(self, email, name, birth_day, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            birth_day=birth_day,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, birth_day, phone_number, password):
        user = self.create_user(
            email,
            name=name,
            birth_day=birth_day,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
