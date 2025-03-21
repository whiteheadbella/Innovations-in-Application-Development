from django.forms import ModelForm
from django import forms
from .models import Employee

class EmployeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'hired': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
