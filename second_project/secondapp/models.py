from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userinfo(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    def __str__(self):
        return self.firstname+" "+self.lastname
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)
    def __str__(self):
        return self.user.username
