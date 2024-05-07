from django.db import models


class Fitness(models.Model):
    rec = models.CharField(max_length = 200)
    rate = models.FloatField(default = 0.0)
    