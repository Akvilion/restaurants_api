# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import os
from rest_framework import status


def one(request):
    return HttpResponse('hello')


class RestaurantsView(APIView):

    t = (os.path.join(os.getcwd(), 'myapi', 'initial_restaurants.json'))
    with open(t, 'r') as f:
        restaurants = json.load(f)

    def get(self, request):
        return Response({"restaurants": self.restaurants})

    def post(self, request):
        serializer = request.data
        self.restaurants.append(serializer)
        return Response(serializer, status=status.HTTP_201_CREATED)
