from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    name = models.CharField(max_length=20)
    task = models.TextField('Описание')
    text = models.TextField('Содержание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
