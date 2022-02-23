from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Car, Driver
from .forms import CarForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here. 
def car_list(request):
    pass

# добавление авто в список, только супер пользователь
def add_car(request):
    submitted = False
    if request.method == 'POST':
        if request.user.is_superuser:
            form = CarForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_car?submitted=True')
    else:
        form = CarForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'blog/add_car.html', {
        'form': form,
        'submitted': submitted,
    })

# профиль пользователя с гаражем 
def profile_garage(request):
    if request.user.is_authenticated:
        me = request.user
        my_car = Car.objects.filter(buyer=request.user)
        return render(request, 'blog/profile_garage.html', {
            "me": me,
            'my_car': my_car,
        })

# базовая страница
def base(request):
    return render(request, 'blog/index.html', {})