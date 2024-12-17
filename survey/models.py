from django.db import models

class SurveyResponse(models.Model):
    name = models.CharField(max_length=100)
    favorite_car = models.CharField(max_length=100)
    preferred_color = models.CharField(max_length=100)
