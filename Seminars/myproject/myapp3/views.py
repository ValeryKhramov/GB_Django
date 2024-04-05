from django.shortcuts import render
from .models import Author
from random import choice, randint
from .forms import GameChoiceForm, AuthorForm
import logging


logger = logging.getLogger('myapp')


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
        my_list.append(randint(1, 6))

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


def game_choice(request):
    if request.method == 'POST':
        form = GameChoiceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            count = form.cleaned_data['count']

            logger.info(f'Получили: {name=}, {count=}')
            match name:
                case 'coin':
                    return coin(request, count)
                case 'cub':
                    return cub(request, count)
                case 'numbers':
                    return numbers(request, count)
    else:
        form = GameChoiceForm()
    return render(request, 'myapp3/game_choice.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            second_name = form.cleaned_data['second_name']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']

            logger.info(f'Получили: {name=}, {second_name=}, {email=}, {biography=}, {birthday=}')

            author = Author(name=name, second_name=second_name, email=email, biography=biography, birthday=birthday)
            author.save()
            message = 'Автор успешно сохранен'
    else:
        form = AuthorForm()
        message = 'Введите данные об авторе'
    return render(request, 'myapp3/add_author.html', {'form': form, 'message': message})