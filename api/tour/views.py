from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tour.models import *
from hotel.models import *

from .serializers import *

class HomePageView(APIView):

    def get(self, request):
        tour = Tour.objects.all()
        serializer = TourSerializer(tour, many=True)
        return Response(serializer.data)