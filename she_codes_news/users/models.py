from django.db import models
from django.conf import settings

#create your models here
from django.contrib.auth.models import AbstractUser

#Abstract User is a default user ( Authentitication functionality)
class CustomUser(AbstractUser):
   bio = models.TextField(blank=True)
   pass

   def __str__(self):
       return self.username

#1) Create a user ProfileModel
   
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #associate one user to one profile
    bio = models.TextField()
    
    def __str__(self):
       return self.user.username
                                     