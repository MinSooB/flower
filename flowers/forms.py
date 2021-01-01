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
            "classification",
        )
        
        widgets = {"name": forms.TextInput(attrs={"placeholder": "꽃 이름"}),
        "date": forms.DateTimeInput(attrs={"placeholder": "날짜. (예시: 2020-12-26)"}),
        "description": forms.TextInput(attrs={"placeholder": "사진 설명"}),
        }
    
    def save(self, *args, **kwargs):
       flower = super().save(commit=False)
       return flower
    
class EditFlowerForm(forms.ModelForm):
    class Meta:
        model = models.Flower
        fields = (
            "name",
            "date",
            "description",
            "classification",
        )
        widgets = {"name": forms.TextInput(attrs={"placeholder": "꽃 이름"}),
        "date": forms.DateTimeInput(attrs={"placeholder": "날짜. (예시: 2020-12-26)"}),
        "description": forms.TextInput(attrs={"placeholder": "사진 설명"}),
        }