from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number_phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number_phone = models.CharField(validators=[number_phone_regex], max_length=16, unique=True)
    address = models.CharField(max_length=100)
    registration_date = models.DateField()

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Number_phone: {self.number_phone},' \
               f' Address: {self.address}, Registration_date: {self.registration_date}.'


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count_products = models.IntegerField()
    date_added = models.DateField()

    def __str__(self):
        return f'Name:{self.name}, Price: {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_of_registration = models.DateField()

    def __str__(self):
        return f'Client: {self.client}, Product: {self.product},' \
               f' Order_price: {self.order_price}, Date_of_registration: {self.date_of_registration}'
