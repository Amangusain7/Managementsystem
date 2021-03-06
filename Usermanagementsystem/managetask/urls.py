from managetask import views
from django.urls import path,re_path

urlpatterns = [
    path('task',views.rolebasedTask.as_view()),
    path('subtask',views.subtask.as_view())
]