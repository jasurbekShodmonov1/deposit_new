from django.db import models


class Prediction(models.Model):
    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    prediction = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
