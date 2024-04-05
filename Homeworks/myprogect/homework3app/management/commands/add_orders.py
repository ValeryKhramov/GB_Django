from django.core.management.base import BaseCommand
from random import uniform, randint, choice
from datetime import timedelta
from django.utils.timezone import now
from homework3app.models import Product, Client, Order
from decimal import Decimal


class Command(BaseCommand):
    help = 'Заполнение таблицы Order тестовыми данными с последующем сохранением БД.'

    def add_arguments(self, parser):
        parser.add_argument('count_orders', type=int, help='Количество заказов')

    def handle(self, *args, **options):
        clients = Client.objects.all()
        products = Product.objects.all()
        orders_start = len(Order.objects.all())
        orders_count = options.get('count_orders')

        for i in range(orders_start + 1, orders_start + orders_count + 1):
            products_to_order = [choice(products) for _ in range(randint(1, 5))]
            order = Order(
                client=choice(clients),
                order_price=0,
                date_of_registration=now() - timedelta(
                    days=randint(1, 200),
                    hours=randint(1, 23),
                    minutes=randint(0, 59)
                )
            )
            order.save()
            order.product.set(products_to_order)
            order.order_price = sum([Decimal(item.price) for item in order.product.all()])
            order.save()

        self.stdout.write(f'В таблицу Order успешно добавлено {orders_count} записей.')
