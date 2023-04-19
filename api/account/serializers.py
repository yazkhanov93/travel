from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import *



class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "referal_user","password"]


class UserSerializerWithToken(UserCreateSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ["id", "username","token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "referal_user"]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = "__all__"