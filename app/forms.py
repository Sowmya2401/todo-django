from django import forms
from . models import items
from django.forms import TextInput

class formForm(forms.ModelForm):
    class Meta:
        model=items
        fields = ['name']
        widgets={
            'name': TextInput(attrs={
                "type":"text",
                "class":"form-control",
                "placeholder":"Type here.",
                "aria-describedby":"basic-addon1",
                "name":"todo"
            })
        
        }
