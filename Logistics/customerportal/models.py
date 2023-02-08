from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    userid = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    city = models.CharField(max_length=120)
    province = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    address = models.TextField(null = True)
    postal = models.IntegerField()
    contact = models.IntegerField()
    cnic = models.IntegerField()
    
    def __str__(self):
        return self.userid.username
    

class Rider(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
    name = models.CharField(max_length=120)
    contact = models.IntegerField()
    cnic = models.IntegerField()
    
    def __str__(self):
        return str(self.name) 

class Status(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return str(self.name) 
        
class ServiceType(models.Model):
    name = models.CharField(max_length=120)
    charges = models.FloatField(max_length=120)
    estimateTime = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

class Parcel(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceType,on_delete=models.CASCADE)
    weight = models.FloatField()
    qty = models.IntegerField()
    pickuplocation = models.TextField(max_length=200,null = True)
    deliverlocation = models.TextField(max_length=200,null = True)
    city = models.CharField(max_length=120,null = True)
    country = models.CharField(max_length=120,null = True)
    state = models.CharField(max_length=120,null = True)
    total = models.FloatField(max_length=120,null = True)
    consigneeName = models.CharField(max_length=120,null = True)
    consigneeEmail = models.CharField(max_length=120,null = True)
    consigneeContact = models.IntegerField(null = True)
    PaymentStatus = models.CharField(max_length=120,null = True)
    date = models.DateTimeField(auto_now_add=True,null = True)
    pcity = models.CharField(max_length=120,null = True)
    pcountry = models.CharField(max_length=120,null = True)
    pstate = models.CharField(max_length=120,null = True)
    
    def __str__(self):
        return str(self.customer) +" \t  "+ str(self.date)
    
class AssignParcel(models.Model):
        parcel = models.ForeignKey(Parcel,on_delete=models.CASCADE)
        rider = models.ForeignKey(Rider,on_delete=models.CASCADE)

