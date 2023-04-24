from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from api.account.views import * 
from api.tour.views import *
from api.hotel.views import *
from api.order.views import *


urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),

    path("home-page/", HomePageView.as_view(), name="home-page"),
    path("region-list/", RegisonList.as_view(), name="region-list"),
    path("country-list/", CountryList.as_view(), name="country-list"),
    path("city-list/", CityList.as_view(), name="city-list"), 

    path("tour-detail/<int:pk>/", TourDetailView.as_view(), name="tour-detail"),
    path("hotel-list/", HotelList.as_view(), name="hotel-list"),

    path("create-order/", OrderView.as_view(), name="create-order"),
    path("user-order/", UserOrderView.as_view(), name="user-order"),
]