from django.db import models

# Create your models here.

class main(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,null=True)
    domainname=models.CharField(max_length=150)
