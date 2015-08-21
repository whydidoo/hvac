# -*- coding: utf-8 -*-
from django import forms
class shemaoneleto(forms.Form):
    temperatura = forms.CharField(label='Температура', max_length=100)
    entalpiya = forms.CharField(label='Энтальпия', max_length=100)
