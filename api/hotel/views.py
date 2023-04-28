from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from hotel.models import *
from .serializers import *


class HotelList(APIView):
    def get(self, request):
        try:
            hotel = Hotel.objects.all()
            if request.query_params.get("city", None):
                city = request.query_params.get("city", None)
                hotel = hotel.filter(city__title=city)
            if request.query_params.get("min_price", None):
                min_price = request.query_params.get("min_price", None)
                hotel = hotel.filter(price__gte=min_price)
            if request.query_params.get("max_price", None):
                max_price = request.query_params.get("max_price", None)
                hotel = hotel.filter(price__lte=max_price)
            if request.query_params.get("star", None):
                star = request.query_params.get("star", None)
                hotel = hotel.filter(star_count=star)
            if request.query_params.get("booking_rating", None):
                booking_rating = request.query_params.get("booking_rating", None)
                hotel = hotel.filter(booking_rating__gte=booking_rating)
            if request.query_params.get("tripadvisor_rating", None):
                tripadvisor_rating = request.query_params.get("tripadvisor_rating", None)
                hotel = hotel.filter(tripadvisor_rating__gte=tripadvisor_rating)
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
