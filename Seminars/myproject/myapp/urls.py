from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('heads/', views.heads_or_tails, name='heads_or_tails'),
    path('cub/', views.cub, name='cub'),
    path('numbers/', views.numbers, name='numbers'),
]