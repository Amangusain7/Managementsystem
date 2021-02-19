from userRegistration import views
from django.urls import path

urlpatterns = [
    path('register', views.registeruser.as_view()),
]