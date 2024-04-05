from django import forms
from .models import Author
import datetime

class GameChoiceForm(forms.Form):
    name = forms.ChoiceField(choices=(('coin', 'Монета'),
                                      ('cub', ' Кости'),
                                      ('numbers', 'Числа')))
    count = forms.IntegerField(min_value=1, max_value=50)


class AuthorForm(forms.Form):
    # class Meta:
    #     model = Author
    #     fields = ['name', 'second_name', 'email', 'biography', 'birthday']
    name = forms.CharField(max_length=100)
    second_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    birthday = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                          'type': 'date'}))
