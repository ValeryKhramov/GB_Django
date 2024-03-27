from django.http import HttpResponse
from random import choice, randint
from myapp.models import Coin


def index(request):
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("About us")


def heads_or_tails(request):
    choice_coin = Coin(result=choice(['Орёл', 'Решка']))
    choice_coin.save()
    return HttpResponse(choice_coin)


def coin_values(request):
    value = Coin.values()
    result = ''
    for i in value:
        result += str(i) + '<br>'
    return HttpResponse(result)


def cub(request):
    return HttpResponse(str(randint(1, 7)))


def numbers(request):
    return HttpResponse(str(randint(0, 1000)))
