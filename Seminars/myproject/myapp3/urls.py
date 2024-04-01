from django.urls import path
from .views import index, about, main, cub, coin, numbers

urlpatterns = {
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('main/', main, name='main'),
    path('cub/<int:count>/', cub, name='cub'),
    path('coin/<int:count>/', coin, name='coin'),
    path('numbers/<int:count>/', numbers, name='numbers'),
}
