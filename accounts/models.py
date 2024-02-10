from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    job = models.CharField(max_length=200)
    
    
    def __str__(self):
        return f"{self.name} - {self.job} - {self.age}"
    