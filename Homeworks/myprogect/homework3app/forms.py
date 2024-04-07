from django import forms
import datetime


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=150, widget=forms.Textarea())
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count_products = forms.IntegerField()
    date_added = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField()
