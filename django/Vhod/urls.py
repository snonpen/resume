from django.urls import path
from .. import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('secret_page/', views.secret_page, name='secret_page'),
]