from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from hotel.models import *
from .serializers import *


class HotelList(APIView):
    def get(self, request):
        try:
            hotel = Hotel.objects.all()
            serializer = HotelSerializer(hotel, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CityList(APIView):
    def get(self, request):
        try:
            city = City.objects.all()
            serializer = CitySerializer(city, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CountryList(APIView):
    def get(self, request):
        try:
            country = Country.objects.all()
            serializer = CountrySerializer(country, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RegisonList(APIView):
    def get(self, requset):
        try:
            region = Region.objects.all()
            serializer = RegionSerializer(region, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
