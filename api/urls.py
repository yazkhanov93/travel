from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from api.account.views import * 
from api.tour.views import *


urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),

    path("home-page/", HomePageView.as_view(), name="home-page"),

]