from django.db import models
from django.utils import timezone


class File(models.Model):

    file = models.FileField(
        blank=True,
        null=True,
        verbose_name='Файл'
    )
    processed = models.BooleanField(
        default=False,
        verbose_name='Обработан ли'
    )
    uploaded_at = models.DateTimeField(
        verbose_name='Когда загружен',
        default=timezone.now
    )

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return f'{self.id}'
