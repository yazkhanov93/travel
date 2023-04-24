from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import CustomUser


class Point(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="user")
    point = models.FloatField(verbose_name="Балл", default=0)

    class Meta:
        verbose_name_plural = "Баллы пользователя"

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=CustomUser)
def create_point(sender, instance, created, **kwargs):
    if created:
        user_point = Point(user=instance)
        user_point.save()


class PointEarned(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="user_earned")
    point = models.FloatField(verbose_name="Балл", default=0)
    description = models.CharField(max_length=255, verbose_name="Заметка", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name_plural = "Баллы заработанные"

    def __str__(self):
        return self.user.username


class PointSpent(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="user_spent")
    point = models.FloatField(verbose_name="Балл", default=0)
    description = models.CharField(max_length=255, verbose_name="Заметка", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name_plural = "Баллы затраченные"

    def __str__(self):
        return self.user.username