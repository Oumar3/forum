from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Forum (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Discusion (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post (models.Model):
    content = models.TextField()
    discussion = models.ForeignKey(Discusion, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.created_by} on {self.discussion.title}'
