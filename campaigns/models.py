from django.db import models
from users.models import User

class Campagin(models.Model):
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    number_of_funds = models.PositiveIntegerField()
    goal = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='campagins/',blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    
