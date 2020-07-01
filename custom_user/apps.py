from django.apps import AppConfig


class CustomUserConfig(AppConfig):
    name = 'custom_user'

    def ready(self):
        from . import signals
