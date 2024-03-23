import random

from django.http import HttpResponse
from random import choice, randint


def index(request):
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("About us")


def heads_or_tails(request):
    return HttpResponse(choice(['Орёл', 'Решка']))


def cub(request):
    return HttpResponse(str(randint(1, 7)))


def numbers(request):
    return HttpResponse(str(randint(0, 1000)))
