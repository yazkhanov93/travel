from django.db import models
from hotel.models import Region, City, Hotel


class TourCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name="Категория")

    class Meta:
        verbose_name_plural = "Категория туров"

    def __str__(self):
        return self.title


class Tour(models.Model):
    category = models.ForeignKey(TourCategory, on_delete=models.CASCADE, verbose_name="Категория", related_name="tour_category")
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Краткое описание")
    departure_date = models.DateTimeField(auto_now_add=False, verbose_name="Дата вылета")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город", related_name="tour_city")
    hotel = models.ManyToManyField(Hotel, verbose_name="Отели", related_name="tour_hotels", blank=True)
    night = models.PositiveIntegerField(default=1, verbose_name="Количество ночей")
    min_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Минимальная цена")
    sale = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Скидка")

    class Meta:
        verbose_name_plural = "Тур"

    def img(self):
        img = TourImage.objects.filter(tour=self).first()
        return img

    def __str__(self):
        return self.title


class TourImage(models.Model):
    tour =  models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Тур", related_name="tour_image")
    image = models.ImageField(upload_to="tour_img/", blank=True, null=True, verbose_name="Фото")


    class Meta:
        verbose_name_plural = "Тур фото"

    def __str__(self):
        return self.tour.title