from rest_framework import serializers
from account.models import CustomUser
from order.models import *
from api.tour.serializers import TourDetailSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class UserOrderSerializer(serializers.ModelSerializer):
    tour = TourDetailSerializer()
    class Meta:
        model = Order
        fields = "__all__"