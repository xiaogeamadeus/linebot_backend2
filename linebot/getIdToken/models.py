from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    createdAt = models.CharField(max_length=100)
    # the link of picture
    picture = models.CharField(max_length=100)


class Bot(models.Model):
    bot_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    developerId = models.CharField(max_length=100)
    flowChart = models.TextField(max_length=100)
    createdAt = models.CharField(max_length=100)
    updateAt = models.CharField(max_length=100)


class Activation(models.Model):
    bot_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
