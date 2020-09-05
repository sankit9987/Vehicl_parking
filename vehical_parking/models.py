from django.db import models

# Create your models here.
class category(models.Model):
    categoryname = models.CharField(max_length=50)
    def __str__(self):
        return self.categoryname
class vehical(models.Model):
    parkingnumber = models.CharField(max_length=50)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    vehicalcompony = models.CharField(max_length=50)
    ownername = models.CharField(max_length=50)
    ownercontact = models.CharField(max_length=50)
    pdate = models.DateField(auto_now_add=True)
    intime = models.TimeField(auto_now_add=True)
    outtime = models.CharField(max_length=50)
    parkingcharge = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.parkingnumber
