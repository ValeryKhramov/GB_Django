from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 text-align:center>Homework two<h1>")
