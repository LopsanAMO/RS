from django import forms
from .models import usuarios

class RegistroForm(forms.ModelForm):
    class Meta:
        model = usuarios()
        fields = '__all__'
        
