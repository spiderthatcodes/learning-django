from django.db import models

class React(models.Model):
    name = models.CharField(max_length=40)
    detail = models.CharField(max_length=500)
