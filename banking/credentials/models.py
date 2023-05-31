from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(auto_now_add=True)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
