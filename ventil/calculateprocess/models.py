# -*- coding: utf-8 -*- 
from django.db import models

# Create your models here.

class Feedback(models.Model):
    class Meta:
        verbose_name_plural = u"Отзывы по ID диаграмме"
        verbose_name = u"Отзывы по ID диаграмме"

    title       = models.CharField(max_length=200)
    content     = models.TextField()
    date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title
