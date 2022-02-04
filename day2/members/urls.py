
from django.contrib import admin
from django.urls import path
from .views import log_in,log_out,register_Auth
urlpatterns = [
  path('loginAuth/',log_in,name="log-in"),
  path('logoutAuth/',log_out,name="log-out"),
  path('registerAuth/',register_Auth,name="register-Auth"),

]