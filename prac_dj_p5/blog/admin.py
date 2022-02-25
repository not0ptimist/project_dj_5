from django.contrib import admin
from .models import Car, Driver

# Register your models here.
@admin.register(Car)
class Car(admin.ModelAdmin):
    list_display = ['concern', 'model', 'year_release', 'buyer']
    search_fields = ('model', 'vin_car')

# Register Driver.
@admin.register(Driver)
class Driver(admin.ModelAdmin):
    list_display = ['name_driver', 'model_car']