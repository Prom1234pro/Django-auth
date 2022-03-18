import email
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses_name = models.CharField(max_length=50)
    no_of_users = models.IntegerField(default=0)

    def __str__(self):
        return self.courses_name