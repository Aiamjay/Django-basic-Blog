from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def publish(self):
        if self.published:
            self.published_date = None
            self.published = False
        else:
            self.published_date = timezone.now()
            self.published = True
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'pk': self.pk})
