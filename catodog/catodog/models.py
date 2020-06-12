from django.db import models
from django.contrib.auth.models import User


class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vk_id = models.TextField()

    def __str__(self):
        return self.poll_text

