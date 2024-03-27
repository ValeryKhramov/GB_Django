from django.http import HttpResponse
from .models import Author


def index(request):
    return HttpResponse('BlogApp')


def add_author(request):
    for i in range(1, 11):
        author = Author(name=f'Name{i}', last_name=f'Last_name{i}', email=f'email{i}@example.com',
                        biography=f'Biographe{i}', birthday=f'2023-10-{i}')
        author.save()
    return HttpResponse('Таблица успешно заполнена!')
