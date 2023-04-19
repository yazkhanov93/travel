from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from account.models import *
from .serializers import *


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUD)

    @swagger_auto_schema(request_body=ProfileSerializer)
    def put(self, request):
        try:
            data = request.data
            profile = Profile.objects.get(user=request.user)
            serializers = ProfileSerializer(profile, data=data)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterUser(APIView):
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        try:
            data = request.data
            user = CustomUser.objects.create(
                username=data["username"],
                referal_user=data["referal_user"],
                password=make_password(data["password"])
            )
            serializer = UserCreateSerializer(user, many=False)
            return Response(serializer.data)
        except:
            return Response({"Try again"})