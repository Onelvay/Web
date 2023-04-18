from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    city = models.CharField(max_length=20)
    address = models.TextField()
    # def __init__(self,name,description,city,address):
    #     self.name=name
    #     self.description=description
    #     self.city=city
    #     self.address=address
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


