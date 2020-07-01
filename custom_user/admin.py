from django.contrib import admin
from .models import (
    CustomUser,
    RegistrationToken,
    PasswordRestorationToken
)

admin.site.register(CustomUser, admin.ModelAdmin)
admin.site.register(RegistrationToken, admin.ModelAdmin)
admin.site.register(PasswordRestorationToken, admin.ModelAdmin)
