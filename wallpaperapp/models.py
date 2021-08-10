from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    photo=models.ImageField(upload_to="wallpaper")
    date=models.DateTimeField(auto_now_add=True)

class UserDetail(models.Model):

    fn=models.CharField(User,max_length=300)
    ln=models.CharField(User,max_length=300)
    email=models.EmailField(max_length=500, default="someone@mail.com")
    password=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='userimage', default="user.png")
    created=models.DateTimeField(auto_now=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"user id is {self.email}"


