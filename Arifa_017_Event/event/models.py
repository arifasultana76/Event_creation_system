from django.db import models
from django.contrib.auth.models import AbstractUser

class EventUserModel(AbstractUser):
    full_name=models.CharField(max_length=100,null=True)
    profile_image=models.ImageField(upload_to='pics',null=True)
    USER_TYPES=[
        ('Admin','Admin'),
        ('Creator','Creator'),
    ]
    user_types=models.CharField(choices=USER_TYPES,max_length=100,null=True)
    
    def __str__(self):
        return self.username
    
class CategoryModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name
    
class EventModel(models.Model):
    event_title=models.CharField(max_length=100,null=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    description=models.TextField(null=True)
    event_date=models.DateField(null=True)
    STATUS=[
        ('NotStarted','NotStarted'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
    ]
    status=models.CharField(choices=STATUS,max_length=100,null=True)
    created_by=models.ForeignKey(EventUserModel,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.event_title
    
    
    


