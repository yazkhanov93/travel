from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.parsers import MultiPartParser, FormParser

from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth.hashers import make_password

from account.models import *
from .serializers import *
from .utils import send_otp


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=ProfileEditSerializer)
    def put(self, request, format=None):
        try:
            data = request.data
            data["user"] = request.user.id
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileEditSerializer(profile, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetOtpView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            otp = send_otp(request)
            return Response(otp)
        else:
            return Response(serializer.errors)


class Register(APIView):
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        # try:
            data=request.data
            user = CustomUser.objects.create(
                username=data["username"],
                referal_user=data["referal_user"],
                password=make_password(data["password"])
            )
            # serializer = UserCreateSerializer(user)
            # serializer = UserCreateSerializer(data=data)
            # if serializer.is_valid():
            #     serializer.save()
            return Response(serializer.data)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)


