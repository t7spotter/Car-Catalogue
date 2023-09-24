from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=128)
    
    def __str__(self):
        return self.title
    
class Company(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
    