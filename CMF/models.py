from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Organization(models.Model):
    name  = models.CharField(max_length=20)
    admin = models.ForeignKey(User, related_name="+")
    

class MoneyUser(models.Model):
#    9999.99
    money = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.OneToOneField(User)
    organization = models.ManyToManyField(Organization, related_name="moneyusers")

class Request(models.Model):
    from_user = models.ForeignKey(User, related_name="+")
    to_from_user = models.ForeignKey(User, related_name="+")
    is_accept = models.BooleanField()
    is_fill   = models.BooleanField()
    request_date = models.DateTimeField()
    accept_date  = models.DateTimeField()
    
    