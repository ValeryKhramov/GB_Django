from django.shortcuts import render
from .models import Coin, Cub, Numbers
from random import choice, randint
import datetime


def index(request):
    context = {'title': 'Фреймворк Django!'}
    return render(request, 'myapp3/index.html', context)


def about(request):
    context = {'title': 'Страница обо мне'}
    return render(request, 'myapp3/about.html', context)


def main(request):
    context = {'title': 'Главная страница'}
    return render(request, 'myapp3/main.html', context)


def numbers(request, count):
    my_list = []

    for i in range(count):
        my_list.append(randint(0,1000))

    context = {'title': 'numbers',
               'my_list': my_list, }
    return render(request, 'myapp3/CCN.html', context)


def cub(request, count):
    my_list = []

    for i in range(count):
        my_list.append(randint(1,6))

    context = {'title': 'cub',
               'my_list': my_list, }
    return render(request, 'myapp3/CCN.html', context)


def coin(request, count):
    my_list = []

    for i in range(count):
        my_list.append(choice(['Орёл', 'Решка']))

    context = {'title': 'coin',
               'my_list': my_list, }
    return render(request, 'myapp3/CCN.html', context)
