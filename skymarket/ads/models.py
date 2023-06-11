from django.conf import settings
from django.db import models


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ad_image', null=True, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['created_at']


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    ad = models.ForeignKey('ads.Ad', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']
