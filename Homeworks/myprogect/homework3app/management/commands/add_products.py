from django.core.management.base import BaseCommand
from random import uniform, randint
from datetime import timedelta
from django.utils.timezone import now
from homework3app.models import Product


class Command(BaseCommand):
    help(f'Заполнение таблицы Product тестовыми данными с последующем сохранением БД.')

    def add_arguments(self, parser):
        parser.add_argument('products_count', type=int, help='Количество товаров')

    def handle(self, *args, **options):
        products_count = options.get('products_count')

        product_start = len(Product.objects.all())

        for i in range(product_start + 1, product_start + products_count + 1):
            product = Product(
                name=f'Product_name_{i}',
                description=f'Product_description_{i}',
                price=round(uniform(1, 5_000), 2),
                count_products=randint(1, 25),
                date_added=now() - timedelta(
                    days=randint(1, 200),
                    hours=randint(1, 23),
                    minutes=randint(0, 59)
                )
            )
            product.save()

        self.stdout.write(f"В таблицу Product успешно добавлено {products_count} записей.")
