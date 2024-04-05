from django.core.management.base import BaseCommand
from homework3app.models import Client


class Command(BaseCommand):
    help = 'Очиcтка таблицы Client с последующем сохранением БД.'

    def handle(self, *args, **options):
        clients = Client.objects.all()

        for item in clients:
            item.delete()

        self.stdout.write('Таблица Client успешно очищена.')
