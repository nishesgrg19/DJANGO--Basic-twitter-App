from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=50,blank=False)
    content=models.TextField(blank=False)
    date=models.DateField(auto_now_add=True)
    is_completed=models.BooleanField()
    author=models.ForeignKey(User,on_delete=CASCADE)
    def __str__(self) :
        return self.title
    
