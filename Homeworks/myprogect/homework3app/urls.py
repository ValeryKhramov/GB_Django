from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('get_clients', read_clients, name='get_clients'),
    path('create_client/<str:name>/<str:email>/<str:number_phone>/<str:address>/', create_client, name='create_client'),
    path('delete_client/<int:pk>/', delete_client, name='delete_client'),
    path('get_products', read_products, name='read_products'),
    path('create_product/<str:name>/<str:description>/<int:price>/<int:count_products>/', create_product,
         name='create_product'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('orders_by_id/<int:pk>/', orders_by_id, name='orders_by_id'),
    # Работа с выводом и сортировкой заказов клиента
    path('orders_client_for_weak/<int:pk>/<int:time>', orders_client_by_time, name='orders_client_by_time'),


]
