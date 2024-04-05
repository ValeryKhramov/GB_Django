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


class Author(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'Name: {self.name}, Second_name: {self.second_name}, Email: {self.email}, Birthday: {self.birthday}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'
