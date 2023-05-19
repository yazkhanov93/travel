import random
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
from .utils import *

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

class Register(APIView):
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        try:
            data=request.data
            user = CustomUser.objects.create(
                username=data["username"],
                referal_user=data["referal_user"],
                password=make_password(data["password"])
            )
            send_otp(data["username"])
            serializer = UserSerializerWithToken(user)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VerifyOtpView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyOtpSerializer(data=data)
            if serializer.is_valid():
                user = CustomUser.objects.get(username=request.user)
                user.is_verified = True
                user.save()
            return Response()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetPasswordResetCodeView(APIView):
    def post(self, request):
        try:
            data = request.data
            username = data["username"]
            user = CustomUser.objects.get(username=username)
            otp = user.otp
            password_reset_otp(otp, username)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    def post(self, request):
        try:
            data=request.data
            serializer = PasswordResetSerializer(data=data)
            if serializer.is_valid():
                user = CustomUser.objects.get(username=data["username"])
                if user.otp == data["otp"]:
                    user.password = make_password(data["password"])
                    otp = random.randint(1000, 9999)
                    user.otp = otp
                    user.save()
                else:
                    return Response({"otp is not valid"})
                return Response({"Password was changed"})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)