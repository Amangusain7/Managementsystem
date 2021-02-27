from managetask import views
from django.urls import path

urlpatterns = [
    path('task',views.rolebasedTask.as_view())
]