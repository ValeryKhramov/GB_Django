from django.db import models
from datetime import date


class Client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    number_phone = models.IntegerField(blank=False)
    address = models.CharField(max_length=100, blank=False)
    registration_date = models.CharField(default=date.today(), max_length=12)

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Number_phone: {self.number_phone},' \
               f' Address: {self.address}, Registration_date: {self.registration_date}.'


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count_products = models.IntegerField()
    date_added = models.CharField(default=date.today(), max_length=12)

    def __str__(self):
        return f'Name:{self.name}, Description: {self.description}, Price: {self.price},' \
               f' Count_products: {self.count_products}, Date_added: {self.date_added}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_of_registration = models.CharField(default=date.today(), max_length=12)

    def __str__(self):
        return f'Client: {self.client}, Product: {self.product},' \
               f' Order_price: {self.order_price}, Date_of_registration: {self.date_of_registration}'
