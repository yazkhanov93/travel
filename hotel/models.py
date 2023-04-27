from django.db import models
from manager_contact.models import *


class Region(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name_plural = "Регионы"

    def __str__(self):
        return self.title

class Country(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион", related_name="country_region")
    title = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.title


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Страна", related_name="region_city")
    title = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to="city_img/", verbose_name="Фото", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Города"

    def __str__(self):
        return self.title


class Hotel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город", related_name="hotel_city")
    star_count = models.PositiveIntegerField(default=1, verbose_name="Количества звезд")
    booking_rating = models.FloatField(verbose_name="Рейтинг отеля на Booking")
    tripadvisor_rating = models.FloatField(verbose_name="Рейтинг отеля на Tripadvisor")
    point = models.FloatField(verbose_name="Количество баллов")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Минимальная цена за номер")
    link = models.CharField(max_length=255, verbose_name="Опмсание на другом сайте", blank=True, null=True)
    whatsapp = models.ForeignKey(ManagerContact, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Отели"

    def __str__(self):
        return self.title


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Отель", related_name="hotel_image")
    image = models.ImageField(upload_to="hotel_img/", verbose_name="Фото")

    class Meta:
        verbose_name_plural = "Отель Фото"

    def __str__(self):
        return self.hotel.title