from django.shortcuts import render, get_object_or_404
from .models import Product, Client, Order
from django.http import HttpResponse
from datetime import timedelta
from django.utils.timezone import now


# Базовая страница
def index(request):
    context = {'title': 'Базовая страница!'}
    return render(request, 'homework3app/base.html', context)


def orders_by_id(request, pk):
    orders_list = Order.objects.filter(client=pk)
    client = Client.objects.filter(pk=pk).first()
    context = {
        'title': 'Заказы клиента',
        'orders_list': orders_list,
        'name': client.name,
        'number_phone': client.number_phone,
        'address': client.address,
        'client': client
    }
    return render(request, 'homework3app/order_by_id.html', context)


def orders_client_by_time(request, pk, time):
    customer = get_object_or_404(Client, pk=pk)
    orders = Order.objects.filter(client=customer,
                                  date_of_registration__gt=now() - timedelta(days=int(time)))
    print(now() - timedelta(days=int(time)))
    products = set([p for o in orders for p in o.product.all()])
    products = list(products)
    match time:
        case 7:
            message = 'Заказы клиента за неделю'
        case 30:
            message = 'Заказы клиента за месяц'
        case 365:
            message = 'Заказы клиента за год'

    context = {'message': message,
               'my_list': products}
    return render(request, 'homework3app/orders_client_by_time.html', context)


# Работа с КЛИЕНТАМИ
def read_clients(request):
    clients_list = list(Client.objects.all())
    context = {
        'title': 'Получение списка клиентов',
        'my_list': clients_list,
    }
    return render(request, 'homework3app/clients_read.html', context)


def create_client(request, name, email, number_phone, address):
    context = {
        'title': 'Добавление клиента',
        'result': 'Клиент успешно добавлен!',
    }
    client = Client(name=name, email=email, number_phone=number_phone, address=address)
    client.save()
    return render(request, 'homework3app/client_cud.html', context)


def delete_client(request, pk):
    context = {
        'title': 'Удаление клиента',
        'result': f'Клиент c id = {pk} удален',
    }
    client = Client.objects.filter(pk=pk).first()
    client.delete()
    return render(request, 'homework3app/client_cud.html', context)


def clear_clients(request):
    list_client = list(Client.objects.all())
    for item in list_client:
        item.delete()
    context = {
        'title': 'Удаление всех клиентов',
        'result': 'Все клиенты удалены!'
    }
    return render(request, 'homework3app/client_cud.html', context)


# Работа с ПРОДУКТАМИ
def read_products(request):
    products_list = list(Product.objects.all())
    context = {
        'title': 'Получение БД Products',
        'my_list': products_list
    }
    return render(request, 'homework3app/products_read.html', context)


def create_product(request, name, description, price, count_products):
    product = Product(name=name, description=description, price=price, count_products=count_products)
    product.save()
    context = {
        'title': 'Добавление продукта',
        'result': 'Продукт успешно добавлен!'
    }
    return render(request, 'homework3app/products_cud.html', context)


def delete_product(request, pk):
    context = {
        'title': 'Удаление продукта',
        'result': f'Продукт с id = {pk} успешно удален!',
    }
    product = Product.objects.filter(pk=pk).first()
    product.delete()
    return render(request, 'homework3app/products_cud.html', context)


# Работа с ЗАКАЗАМИ

def create_order(request):
    pass


def read_orders(request):
    pass


def delete_order(request):
    pass
