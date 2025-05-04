from django.db import models

# Create your models here.
from django.utils import timezone

class City(models.Model):
    name = models.CharField(max_length=100)
    searched_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name