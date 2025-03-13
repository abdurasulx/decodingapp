from django.db import models
class Savol(models.Model):
    title=models.TextField(max_length=255,blank=False)
    des=models.TextField(max_length=1255,blank=False)
    id=models.BigAutoField(primary_key=True)
    answer=models.TextField(max_length=255,blank=False)
    def __str__(self):
        return  f'{self.title}'
class Usr(models.Model):
    log=models.TextField(max_length=255,blank=False,null=False)
    pas=models.TextField(max_length=255,blank=False,null=False)
    lvl=models.IntegerField(default=1)

# Create your models here.
