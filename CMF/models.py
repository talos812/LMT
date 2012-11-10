from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Organization(models.Model):
    name  = models.CharField(max_length=20)
    admin = models.ForeignKey(User, related_name="+")
    def __unicode__(self):
        return self.name
    

class MoneyUser(models.Model):
#    9999.99
    money = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.OneToOneField(User)
    organization = models.ManyToManyField(Organization, related_name="moneyusers")
    def __unicode__(self):
        return "%s has %f"%(self.owner,self.money)

class Request(models.Model):
    from_user = models.ForeignKey(User, related_name="+")
    to_user = models.ForeignKey(User, related_name="+")
    money = models.DecimalField(max_digits=6, decimal_places=2)
    is_accept = models.BooleanField()
    is_fill   = models.BooleanField()
    reason    = models.TextField(null=True,blank=True)
    request_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s give %s money:%f"%(self.from_user,self.to_user, self.money)
#    accept_date  = models.DateTimeField(null=True)
    
    