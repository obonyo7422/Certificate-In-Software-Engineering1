from django import forms
from django.forms import ModelForm
from .models import Customer

class CustomerForm(forms.ModelForm):
    date_of_birth = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Customer
        fields = ['first_name','last_name','date_of_birth','gender','country','state_district','town','zip_code','phone_number','email']