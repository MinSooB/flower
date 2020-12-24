from django.contrib import admin
from . import models

@admin.register(models.Flower)
class FlowerAdmin(admin.ModelAdmin):
    pass