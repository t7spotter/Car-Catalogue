from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=128)
    
    def __str__(self):
        return self.title
    
class Company(models.Model):
    name = models.CharField(max_length=128)
    made_in = models.CharField(max_length=128)
    
    class Meta:
        db_table = "Company"
    def __str__(self):
        return self.name

class Car(models.Model):
    title = models.CharField(max_length=128)
    about = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)