from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('about/', views.about_me, name='about_me'),
]