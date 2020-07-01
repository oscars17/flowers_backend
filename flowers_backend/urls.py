from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('custom_user.urls')),
    path('api/articles/', include('text_materials.urls'))
]
