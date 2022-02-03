
from django.contrib import admin
from django.urls import path
from .views import log_in
urlpatterns = [
  path('loginAuth/',log_in,name="log-in")
]