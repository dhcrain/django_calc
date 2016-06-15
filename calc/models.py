from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Operation(models.Model):
    user = models.ForeignKey(User)
    num1 = models.FloatField()
    operator = models.CharField(max_length=3)
    num2 = models.FloatField()
    result = models.FloatField()
