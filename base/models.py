from django.db import models

# Create your models here.

class Product(models.Model):
    ctg = models.CharField(max_length=50,null=True,blank=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
 
    def __str__(self):
           return self.desc