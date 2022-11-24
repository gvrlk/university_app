from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    name = models.CharField(
        max_length=80,
        help_text='Название комнаты',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Дата создания чата',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Дата обновления чата',
    )

