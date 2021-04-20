from django.urls import path
from myapi import views


app_name = 'myapi'

urlpatterns = [
    path('', views.RestaurantsView.as_view(), name='one'),
]
