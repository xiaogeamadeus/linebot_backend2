from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    # the link of picture
    picture = models.CharField(max_length=100)


class Bot(models.Model):
    bot_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    flowchart = models.TextField(max_length=100)
    is_public = models.BooleanField(default=False)
    created_at = models.CharField(max_length=100)
    update_at = models.CharField(max_length=100)
    # Foreign key
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Activation(models.Model):
    # Foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
