from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone


class Notes(models.Model):
    title = models.TextField(max_length=100)
    details = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
