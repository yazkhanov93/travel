from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import *


class PasswordResetSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    otp = serializers.CharField(max_length=5)
    password = serializers.CharField(max_length=255)


class VerifyOtpSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=5)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username","referal_user","password"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username","referal_user"]


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ["username", "referal_user", "token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ReferalUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    referal_user = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = "__all__"

    def get_referal_user(self, obj):
        referal_user = Profile.objects.filter(user__referal_user=obj.user.username)
        return ReferalUserProfileSerializer(referal_user, many=True).data