from django.contrib.auth.backends import ModelBackend
from custom_user.models import CustomUser


class CustomUserBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        slug = kwargs['slug']
        password = kwargs['password']
        try:
            user = CustomUser.objects.get(slug=slug)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            pass
