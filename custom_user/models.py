from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
from django.utils.text import slugify
from rest_framework import status
import uuid


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")

        slug = slugify(username)
        user = self.model(
            username=username,
            slug=slug,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self, username, email, password=None):
        slug = slugify(username)
        user = self.model(
            username=username,
            slug=slug,
            email=self.normalize_email(email)
        )
        user.is_admin = True
        user.is_active = True
        user.set_password(password)
        user.save(self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=25, verbose_name='username')
    slug = models.SlugField(
        max_length=25,
        blank=True,
        null=True,
        unique=True,
        verbose_name='slug'
        )
    username_changed = models.BooleanField(default=False, verbose_name='username was changed')
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    registration_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.slug

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
       return self.is_admin

    def has_module_perms(self, app_label):
       return self.is_admin


class TokenMeta(models.Model):
    class Meta:
        abstract = True

    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE,
                                editable=False,
                                verbose_name='user'
                                )
    token = models.TextField(verbose_name='token')
    created = models.DateTimeField(blank=True, null=True, verbose_name='created')

    def save(self, *args, **kwargs):
        self.token = str(uuid.uuid3(uuid.NAMESPACE_DNS, self.user.username))
        self.created = timezone.now()
        return super().save(*args, **kwargs)

    def check_signing(self):
        difference = timezone.now() - self.created
        if 72 - difference.total_seconds() / 36000 >= 72:
            return status.HTTP_403_FORBIDDEN
        return status.HTTP_200_OK


class RegistrationToken(TokenMeta):
    def __str__(self):
        return 'Activation token of user {0}'.format(self.user.username)


class PasswordRestorationToken(TokenMeta):
    def __str__(self):
        return 'Password restoration token of user {0}'.format(self.user.username)
