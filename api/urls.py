from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from api.account.views import * 
# from api.tour.views import *


urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),

    path("profile/", UserProfile.as_view(), name="profile"),

    # path("tour-categories/", TourCategoryList.as_view(), name="tour-categories"),
    # path("cities/", CityList.as_view(), name="cities"),
    # path("regions/", RegionList.as_view(), name="regions")
]