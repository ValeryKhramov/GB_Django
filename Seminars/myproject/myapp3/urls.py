from django.urls import path
from .views import index, about, main, cub, coin, numbers, game_choice, add_author

urlpatterns = {
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('main/', main, name='main'),
    path('cub/<int:count>/', cub, name='cub'),
    path('coin/<int:count>/', coin, name='coin'),
    path('numbers/<int:count>/', numbers, name='numbers'),
    path('game_choice/', game_choice, name='game_choice'),
    path('add_author/', add_author, name='add_author'),
}
