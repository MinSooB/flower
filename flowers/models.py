from django.db import models
from django.urls import reverse
from users import models as user_models

class Flower(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(null=True, blank=True)
    photographer = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    photo = models.ImageField(default = '', upload_to="flower_photos")
    
    classification_choices = (("Flower", "Flower"), ("Family", "Family"), ("Others", "Others"))

    classification = models.CharField(
        choices=classification_choices, max_length=10, null=True, blank=True
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("flower:detail", kwargs={"pk": self.pk})

    def first_photo(self):
        try:
            photo = self.photo
            return photo.url
        except ValueError:
            return None
    