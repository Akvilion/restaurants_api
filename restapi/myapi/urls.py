from django.urls import path
from myapi import views


urlpatterns = [
    path('', views.one, name='one'),
]
