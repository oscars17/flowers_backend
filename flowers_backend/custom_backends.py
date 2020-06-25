from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from custom_user.models import CustomUser


class CustomUserBackend(ModelBackend):
    def authenticate(self, **kwargs):
        slug = kwargs['slug']
        password = kwargs['password']
        try:
            user = CustomUser.objects.get(Q(slug=slug) | Q(email=slug))
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            pass
