from django import forms
from .models import fruits, vegetables, kidsitem


class fruitsform(forms.ModelForm):
    class Meta:
        model = fruits
        fields = ['name', 'disc', 'rate', 'pic']


class vegform(forms.ModelForm):
    class Meta:
        model = vegetables
        fields = ['name', 'disc', 'rate', 'pic']


class kidform(forms.ModelForm):
    class Meta:
        model = kidsitem
        fields = ['name', 'disc', 'rate', 'pic']
