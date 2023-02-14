from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/tasks/', views.task_list, name='task_list'),
    path('<str:username>/tasks/<int:pk>/', views.task_detail, name='task_detail'),
]