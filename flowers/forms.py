from django import forms
from . import models

class CreateFlowerForm(forms.ModelForm):
    class Meta:
        model = models.Flower
        fields = (
            "photo",
            "name",
            "date",
            "description",
        )
        
        widgets = {"name": forms.TextInput(attrs={"placeholder": "Name of the Flower"}),
        "date": forms.DateTimeInput(attrs={"placeholder": "0000-00-00 (Date of the Picture Taken)"}),
        "description": forms.TextInput(attrs={"placeholder": "Description of the Picture"}),
        }
    
    def save(self, *args, **kwargs):
       flower = super().save(commit=False)
       return flower