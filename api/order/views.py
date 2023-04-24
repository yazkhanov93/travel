from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from tour.models import *
from hotel.models import *

from .serializers import *

class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            data = request.data
            data["user"] = request.user.id
            hotel = Hotel.objects.get(id=data["hotel"])            
            data["total_price"] = hotel.price * data["person_count"]
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserOrderView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            order = Order.objects.filter(user=request.user)
            serializer = UserOrderSerializer(order, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)