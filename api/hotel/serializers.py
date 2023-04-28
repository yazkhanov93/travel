from rest_framework import serializers
from hotel.models import *


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Region
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    class Meta:
        model = Country
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = City
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    images = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = "__all__"

    def get_images(self, obj):
        images = HotelImage.objects.filter(hotel=obj)
        return HotelImageSerializer(images, many=True).data
