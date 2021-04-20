from django.urls import path
from myapi import views


app_name = 'myapi'

urlpatterns = [
    path('', views.RestaurantsView.as_view(), name='restaurants'),
    path('sorted/', views.RestaurantsSort.as_view(), name='sorted'),
    path('luxury/', views.RestaurantLuxury.as_view(), name='luxury'),
]
