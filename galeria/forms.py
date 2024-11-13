from django import forms
from .models import *


class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',
        }
