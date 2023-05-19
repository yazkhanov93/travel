from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.parsers import MultiPartParser, FormParser

from task.models import *

from .serializers import *


class TaskList(APIView):
    def get(self, request):
        try:
            tasks = Task.objects.all().only("id","title","point")
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TaskDetailView(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskDetailSerializer(task, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TaskDoneList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            tasks = TaskDone.objects.filter(user=request.user)
            serializer = TaskDoneSerializer(tasks, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)



class TaskDoneDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            task = TaskDone.objects.get(id=pk)
            serializer = TaskDoneDetailSerializer(task, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HHTTP_404_NOT_FOUND)
