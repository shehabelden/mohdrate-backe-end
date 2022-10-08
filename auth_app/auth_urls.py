from django.contrib import admin
from django.urls import path
from auth_app.api import *
urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('users/', MainUser.as_view()),
]
