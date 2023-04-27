from django.db import models


class ManagerContact(models.Model):
    title = models.CharField(max_length=100, verbose_name="Менеджер")
    whatsapp = models.CharField(max_length=255, verbose_name="whatsapp_link")

    class Meta:
        verbose_name_plural = "Менеджер WhatsApp"

    def __str__(self):
        return self.title