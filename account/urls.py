from django.urls import path
from .views import (register,login,home)
urlpatterns = [
    path('',home,name="home"),
    path('register/',register, name = 'RegisterForm'),
    path('login/',login, name = 'LoginForm')
]
