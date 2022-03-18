from lib2to3.pgen2 import driver
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Car, Driver
from .forms import CarForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here. 
# Добавление авто в список, только супер пользователь.
def add_car(request):
    submitted = False
    if request.method == 'POST':
        if request.user.is_superuser:
            form = CarForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "You add car")
                return HttpResponseRedirect('add_car?submitted=True')
    else:
        form = CarForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'blog/add_car.html', {
        'form': form,
        'submitted': submitted,
    })

# Профиль пользователя с гаражем.
def profile_garage(request, id_driver):
    if request.user.is_authenticated:
        driver = User.objects.get(id=id_driver)
        car = Car.objects.filter(buyer=driver)
        my_car = car.select_related('buyer')
    else:
        messages.success(request, "You aren't autorized")
        return redirect('login')
    return render(request, 'blog/profile_garage.html', {
        'my_car': my_car,
        'driver': driver,
    })


# Базовая страница.
def base(request):
    driver = request.user
    return render(request, 'blog/index.html', {
        'driver': driver,
    })