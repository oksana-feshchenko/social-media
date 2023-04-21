from django.db import models

from social_media_api import settings


class Tag(models.Model):
    word = models.CharField(max_length=30)


class Post(models.Model):
    text = models.TextField()
    tags = models.ManyToManyField(to=Tag, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.text[:10] + "..."

