from django import forms
from . import models

class CreateFlowerForm(forms.ModelForm):
    class Meta:
        model = models.Flower
        fields = (
            "photo",
            "name",
            "description",
        )
        
        widgets = {"name": forms.TextInput(attrs={"placeholder": "꽃의 이름"}),
        "description": forms.TextInput(attrs={"placeholder": "사진에 대한 설명"}),
        }
    
    def save(self, *args, **kwargs):
       flower = super().save(commit=False)
       return flower