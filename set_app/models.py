
from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length = 40, verbose_name = "Названия")
    description = models.TextField(verbose_name = 'Описание')
    send_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата и Времия публикация')


class Delete(models.Model):
    delete_title = models.CharField(max_length = 40, verbose_name = "Названия")
    delete_description = models.TextField(verbose_name = 'Описание')
    delete_send_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата и Времия публикация')

class Izbran(models.Model):
    izbran_title = models.CharField(max_length = 40, verbose_name = "Названия")
    izbran_description = models.TextField(verbose_name = 'Описание')
    izbran_send_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата и Времия публикация')