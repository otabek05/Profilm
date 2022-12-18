from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=240)


    def __str__(self) -> str:
        return self.name

class Film(models.Model):
    title=models.CharField(max_length=240)
    description=models.TextField()
    owner=models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    img=models.ImageField(upload_to='films/')
    category=models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)

    created=models.DateTimeField(auto_now_add=True,null=True)
    

    
