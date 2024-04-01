from django.core.management.base import BaseCommand
from homework2app.models import Client


class Command(BaseCommand):
    help = "Get clients!"

    def handle(self, *args, **kwargs):
        for client in Client.objects.all():
            self.stdout.write(f'{client}')
