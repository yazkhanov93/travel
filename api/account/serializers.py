from rest_framework import serializers

from account.models import *


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username","referal_user","password"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username","referal_user"]


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