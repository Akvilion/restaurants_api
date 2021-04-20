from rest_framework.views import APIView
from rest_framework.response import Response
import json
import os
from rest_framework import status


class InitRestaurants():

    t = (os.path.join(os.getcwd(), 'myapi', 'initial_restaurants.json'))
    with open(t, 'r') as f:
        restaurants = json.load(f)


class RestaurantsView(APIView):

    def get(self, request):
        return Response({"restaurants": InitRestaurants.restaurants})
 
    def post(self, request):
        serializer = request.data
        InitRestaurants.restaurants.append(serializer)
        return Response(serializer, status=status.HTTP_201_CREATED)


class RestaurantsSort(APIView):

    def get(self, request):
        all = InitRestaurants.restaurants
        sorted_restaurants = sorted(all, key=lambda k: k['rank'], reverse=True)
        return Response({"sorted": sorted_restaurants})


class RestaurantLuxury(APIView):

    def get(self, request):
        all = InitRestaurants.restaurants
        luxury = max(all, key=lambda k: k['average_bill'])
        return Response({"luxury": luxury})
