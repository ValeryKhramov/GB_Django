from django.core.management.base import BaseCommand
from homework3app.models import Product


class Command(BaseCommand):
    help = 'Очиcтка таблицы Product с последующем сохранением БД.'

    def handle(self, *args, **options):
        products = Product.objects.all()

        for item in products:
            item.delete()

        self.stdout.write('Таблица Product успешно очищена.')
