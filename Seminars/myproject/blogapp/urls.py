from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_author/', views.add_author, name='add_author'),
]
