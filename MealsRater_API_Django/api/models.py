from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinValueValidator

class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.IntegerField()

    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)
