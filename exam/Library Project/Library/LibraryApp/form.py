from django import forms
from .models import BooksAdd

class BooksAddForm(forms.ModelForm):
    class Meta:
        model = BooksAdd
        fields = '__all__'
        labels = {'image':''}
