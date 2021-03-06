from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Car(models.Model):
    concern = models.CharField(max_length=100)
    model = models.CharField(max_length=255)
    year_release = models.DateField()
    vin_car = models.CharField(max_length=15, unique=True)
    buyer = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    horse_power =models.IntegerField()
    engine_size = models.IntegerField("engine_size in cm3")
    foto_car = models.ImageField(blank=True, null=True, upload_to='images/car/', default= 'media/images/car/def-carPhoto.jpeg',)

    def __str__(self):
        return self.model


# Модель водителя(пользователя), но лучше использовать встроенного User.
class Driver(models.Model):
    description_driver = models.TextField(max_length=500)
    model_car = models.ForeignKey(Car, max_length=100, null=True, on_delete=models.SET_NULL)
    name_driver = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name_driver