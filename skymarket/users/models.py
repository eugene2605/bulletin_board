from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    USER = 'user', _('user')
    ADMIN = 'admin', _('admin')


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=20, verbose_name='имя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия')
    phone = PhoneNumberField(blank=True, verbose_name='телефон')
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name='аватарка')
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

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

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
