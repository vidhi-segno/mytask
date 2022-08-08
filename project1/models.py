from django.conf import settings
from django.db import models

class Width(models.Model):
    width = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.width)
    
class Height(models.Model):   
    height = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return str(self.height)
class UserInput(models.Model):
    a = models.IntegerField(blank=True,null=True)
    b = models.IntegerField(blank=True,null=True)
    output= models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.output)