from django.core.management.base import BaseCommand
from homework2app.models import Client


class Command(BaseCommand):
    help = 'Fake date for Clients'

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help='Count clients')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(1, count + 1):
            client = Client(name=f'client{i}', email=f'{i}@gmail.com', number_phone=i, address=f'{i}street')
            Client.save(client)
        self.stdout.write('База данных CLIENTS успешно заполнена!')
