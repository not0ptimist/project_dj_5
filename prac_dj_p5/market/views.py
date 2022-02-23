from django.shortcuts import render, redirect
from blog.models import Car
from django.contrib import messages


# Create your views here.
# Покупка
def buy_car(request, id_car):
    if request.user.is_authenticated:
        car = Car.objects.get(pk=id_car)
        car.buyer = request.user
        car.save()
        return redirect('market')
    else:
        messages.success(request, "You aren't autorized to buy this car")
        return redirect('login')

# Detail auto
def detail_car(request, id_car):
    detail = Car.objects.get(pk=id_car)
    return render(request, 'market/detail_car.html', {
        'detail': detail,
        })

# список машин которые свободные, их можно купить
def market(request):
    list_car = Car.objects.filter(buyer=None)
    return render(request, 'market/market.html', {
        'list_car': list_car
        })