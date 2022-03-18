from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('profile_garage/<int:id_driver>', views.profile_garage, name='profile_garage'),
    path('add_car', views.add_car, name='add_car'),
]
