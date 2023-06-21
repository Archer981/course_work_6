from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.db.models import TextChoices

from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(TextChoices):
    # TODO закончите enum-класс для пользователя
    USER = 'user', 'Пользователь'
    ADMIN = 'admin', 'Админ'


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='user_image', null=True, blank=True)
    is_active = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # def save(self, *args, **kwargs):
    #     self.set_password(raw_password=self.password)
    #     super().save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
