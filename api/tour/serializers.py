from rest_framework import serializers

from tour.models import *
from hotel.models import *

from api.hotel.serializers import *


class TourCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCategory
        fields = "__all__"

class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = "__all__"

class TourSerializer(serializers.ModelSerializer):
    category = TourCategorySerializer()
    # images = TourImageSerializer()
    image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tour
        fields = ["id","title","departure_date","night", "description","category","min_price", "image", "sale"]

    def get_image(self, obj):
        image = TourImage.objects.filter(tour=obj).first()
        return TourImageSerializer(image).data


class TourDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    hotel = serializers.SerializerMethodField()
    class Meta:
        model = Tour
        fields = "__all__"

    def get_images(self, obj):
        images = TourImage.objects.filter(tour=obj)
        return TourImageSerializer(images, many=True).data

    def get_hotel(self, obj):
        hotel = Hotel.objects.filter(tour_hotels=obj)
        return HotelSerializer(hotel, many=True).data