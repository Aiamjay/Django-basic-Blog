from django.db import models
from django.utils import timezone
from users.models import CustomUser


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        raise NotImplemented
