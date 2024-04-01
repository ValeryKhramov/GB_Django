from django.db import models


class Coin(models.Model):
    result = models.CharField(max_length=100)
    times = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Результат броска: {self.result}, Время броска: {self.times} '


class Cub(models.Model):
    result = models.IntegerField()
    times = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Результат броска: {self.result}, Время броска: {self.times}'


class Numbers(models.Model):
    result = models.IntegerField()
    times = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Результат броска: {self.result}, Время броска: {self.times} '
