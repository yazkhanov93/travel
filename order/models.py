from django.db import models
from account.models import CustomUser

from tour.models import *
from hotel.models import *


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_order", verbose_name="Пользователь")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="tour_order", verbose_name="Тур")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_order", verbose_name="Отель")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    night = models.IntegerField(default=1, verbose_name="Количество ночей")
    person_count = models.IntegerField(default=1, verbose_name="Количество человек")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    
    class Meta:
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.user.username