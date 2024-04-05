from django.core.management.base import BaseCommand
from random import uniform, randint
from datetime import timedelta
from django.utils.timezone import now
from homework3app.models import Client


class Command(BaseCommand):
    help(f'Заполнение таблицы Client тестовыми данными с последующем сохранением БД.')

    def add_arguments(self, parser):
        parser.add_argument('clients_count', type=int, help='Количество клиентов')

    def handle(self, *args, **options):
        clients_count = options.get('clients_count')

        clients_start = len(Client.objects.all())

        for i in range(clients_start + 1, clients_start + clients_count + 1):
            client = Client(
                name=f'Client_name_{i}',
                email=f'mail{i}@mail.com',
                number_phone=f"+7{''.join([str(randint(0, 9)) for _ in range(10)])}",
                address=f'Client_address{i}',
                registration_date=now() - timedelta(
                    days=randint(1, 200),
                    hours=randint(1, 23),
                    minutes=randint(0, 59)
                )
            )
            client.save()

        self.stdout.write(f"В таблицу Client успешно добавлено {clients_count} записей.")
