from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    name = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # the link of picture
    picture = models.TextField(max_length=100)


class Bot(models.Model):
    bot_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    flowchart = models.TextField(max_length=100)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Foreign key
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Activation(models.Model):
    # Foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "user",
            "bot",
        )
