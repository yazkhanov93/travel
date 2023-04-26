from django.db import models
from account.models import CustomUser


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    file = models.FileField(upload_to="task_file/", blank=True, null=True)
    point = models.IntegerField(verbose_name="Количество баллов")

    class Meta:
        verbose_name_plural = "Задании для полученя баллов"
    
    def __str__(self):
        return self.title



class TaskDone(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Название", related_name="task_done")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_task", verbose_name="пользователь")
    file = models.FileField(upload_to="done_task_file/")
    checked = models.BooleanField(default=False, verbose_name="Проверен")
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата")

    class Meta:
        verbose_name_plural = "Выполненные задании"

    def __str__(self):
        return self.title    