from django.conf.urls import url
from . import views

urlpatterns = [
    url('^sign-up/$', view=views.SignUpAPI.as_view()),
    url('^sign-in/$', view=views.SignInAPI.as_view()),
    url('^auth-state/$', view=views.InitAuthStateAPI.as_view()),
]
