
from django.db import models
from datetime import date 

# Create your models here.
class Drawing(models.Model):
    program = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    revision = models.IntegerField(default=0)
    product_category = models.CharField(max_length=10)
    author = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    description = models.TextField()
    comments = models.TextField()

    def __str__(self):
        return self.program

