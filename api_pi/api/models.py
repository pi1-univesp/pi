from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.email