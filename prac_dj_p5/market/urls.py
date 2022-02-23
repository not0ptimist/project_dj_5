from django.urls import path
from . import views

urlpatterns = [
    path('', views.market, name='market'),
    path('detail_car/<id_car>', views.detail_car, name='detail_car'),
    path('buy_car/<id_car>', views.buy_car, name='buy_car'),
]