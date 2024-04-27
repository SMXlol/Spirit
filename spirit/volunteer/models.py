from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField()
    fodder = models.FloatField()
    readme = models.TextField()
    image_url = models.URLField()
    all_rating = models.FloatField(default=0)
    rating = models.JSONField(default=list)  # Используем JSONField для хранения списка оценок
    count_rate = models.IntegerField(default=0)
    walk = models.BooleanField(default=False)
    recommended_food = models.JSONField(default=list)
    recommended_food_weight = models.FloatField()


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    pets = models.ManyToManyField(Pet)
    image_url = models.URLField()
