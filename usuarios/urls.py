from django.urls import path
from . import views

urlpatterns = [
    path(r'cadastro/', views.cadastro, name='cadastro'),
    path(r'login/', views.login, name='login'),
    path(r'home/', views.home, name='home'),
    path(r'', views.home, name='home')

]