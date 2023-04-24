from rest_framework import serializers

from tour.models import *
from hotel.models import *


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = ["image"]

class TourSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tour
        fields = ["id","title","departure_date","night","category","min_price", "image"]

    def get_image(self, obj):
        image = TourImage.objects.filter(tour=obj).first()
        return TourImageSerializer(image).data


class TourDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = Tour
        fields = "__all__"

    def get_images(self, obj):
        images = TourImage.objects.filter(tour=obj)
        return TourImageSerializer(images, many=True).data