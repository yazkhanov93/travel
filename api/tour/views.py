from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tour.models import *
from hotel.models import *


from .serializers import *

class TourList(APIView):

    def get(self, request):
        # try:
            tour = Tour.objects.all().only("id","title","departure_date","night","category","min_price")
            if request.query_params.get("category", None):
                category = request.query_params.get("category", None)
                tour = tour.filter(category=category)
            if request.query_params.get("date", None):
                date = request.query_params.get("date", None)
                tour = tour.filter(date__icontains=date)
            if request.query_params.get("min_price", None):
                min_price = request.query_params.get("min_price", None)
                tour = tour.filter(min_price__gte=min_price)
            if request.query_params.get("max_price", None):
                max_price = request.query_params.get("max_price", None)
                tour = tour.filter(min_price__lte=max_price)
            serializer = TourSerializer(tour, many=True)
            return Response(serializer.data)
        # except:
        #     return Response(status=status.HTTP_404_NOT_FOUND)


class TourDetailView(APIView):
    def get(self, request, pk):
        # try:
            tour = Tour.objects.get(id=pk)
            serializer = TourDetailSerializer(tour, many=False)
            return Response(serializer.data)
        # except:
        #     return Response(status=status.HTTP_404_NOT_FOUND)