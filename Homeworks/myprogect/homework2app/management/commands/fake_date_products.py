from django.core.management.base import BaseCommand
from homework2app.models import Product


class Command(BaseCommand):
    help = 'Fake date for Products'

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help='Count products')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            product = Product(name=f'product{i}', description=f'description{i}', price=i*i*0.5, count_products=i)
            Product.save(product)
        self.stdout.write('База данных PRODUCT успешно заполнена!')
