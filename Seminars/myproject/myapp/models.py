from django.db import models


# from django.utils import timezone


class Coin(models.Model):
    result = models.CharField(max_length=100)
    times = models.DateTimeField(auto_now=True)  # default=timezone.now

    @staticmethod
    def values():
        value = Coin.objects.order_by('-times')[:5]
        return value

    def __str__(self):
        return f'Результат броска монеты: {self.result}. Время броска: {self.times}.'
