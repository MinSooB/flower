from django.db import models
from users import models as user_models
import datetime


class Flower(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    photographer = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    photo = models.ImageField(default = '', upload_to="flower_photos")
    
    def __str__(self):
        return self.name

    def first_photo(self):
        try:
            photo = self.photo
            return photo.url
        except ValueError:
            return None
    