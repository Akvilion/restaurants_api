# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import os


def one(request):
    return HttpResponse('hello')


class RestaurantsView(APIView):

    t = (os.path.join(os.getcwd(), 'myapi', 'initial_restaurants.json'))
    with open(t, 'r') as f:
        restaurants = json.load(f)

    def get(self, request):
        return Response({"restaurants": self.restaurants})
