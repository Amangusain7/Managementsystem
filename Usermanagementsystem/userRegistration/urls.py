from userRegistration import views
from django.urls import path, include, re_path as url

urlpatterns = [
    path('register', views.registeruser.as_view()),
    url('login', views.LoginView.as_view()),
]