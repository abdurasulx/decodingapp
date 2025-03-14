from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Savol(models.Model):
    title=models.TextField(max_length=255,blank=False)
    des=RichTextField(blank=False)
    id=models.BigAutoField(primary_key=True)
    answer=models.TextField(max_length=255,blank=False)
    def __str__(self):
        return  f'{self.title}'
class Usr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lvl=models.IntegerField(default=1)

# Create your models here.
