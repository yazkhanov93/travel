from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# from point.models import Point

class CustomUser(AbstractUser):
    referal_user = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=5, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="user_profile")
    firstname = models.CharField(max_length=20, verbose_name="Имя", blank=True, null=True)
    middlename = models.CharField(max_length=20, verbose_name="Отчества", blank=True, null=True)
    lastname = models.CharField(max_length=20, verbose_name="Фамилия", blank=True, null=True)
    avatar = models.ImageField(upload_to="profile_img/", blank=True, null=True)
    email = models.EmailField(unique=True, max_length=50, verbose_name="Эл. почта", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Профилы"
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
