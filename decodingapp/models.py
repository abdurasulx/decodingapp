from django.db import models
class Savol(models.Model):
    savol=models.TextField(max_length=255,blank=False)
    javob=models.TextField(max_length=255,blank=False)
    def __str__(self):
        return  f'{self.savol}'
class Usr(models.Model):
    log=models.TextField(max_length=255,blank=False,null=False)
    pas=models.TextField(max_length=255,blank=False,null=False)
    lvl=models.IntegerField(default=1)

# Create your models here.
