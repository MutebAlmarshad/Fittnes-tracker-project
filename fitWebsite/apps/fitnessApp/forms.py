from django import forms
from .models import Fitness

class Fitnessform(forms.ModelForm):
        class Meta:
            model = Fitness 
            fields = ['rec','rate']
        
        rec = forms.CharField(
            max_length=200,
            required=True,
            label='Recommendation', 
        )
        
        rate =  forms.FloatField(
        required=True,
        min_value= 0.0,
        max_value = 10.0,
        label='Rating'
    )
                