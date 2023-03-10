from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.post_create, name='post_create'),
    path('update/<int:pk>/', views.post_update, name='post_update'),
]