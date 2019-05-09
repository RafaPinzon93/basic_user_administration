from django import forms
from django.forms import ModelForm

from internationalflavor.iban import IBANFormField

from .models import User


class UserForm(ModelForm):
    iban = IBANFormField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'iban']
        required = ['first_name', 'last_name', 'iban']
