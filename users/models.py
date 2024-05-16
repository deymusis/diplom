from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link1 = models.URLField('Длинная ссылка', max_length=250)
    link2 = models.CharField('Сокращенная ссылка', max_length=250, unique=True)

    def __str__(self):
        return self.link2

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('redirect-link', kwargs={'slug': self.link2})

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'