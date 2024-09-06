
from django import forms
from .models import DataModel

class DataForm(forms.ModelForm):
    class Meta:
        model = DataModel
        fields = ['picture', 'first_name', 'second_name', 'age', 'dob', 'id_number', 'email', 'phone_number', 'address', 'location']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }


 