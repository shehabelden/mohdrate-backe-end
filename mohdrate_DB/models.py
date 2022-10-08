from django.contrib.auth.models import User
from django.db import models
from auth_app.models import akhtbar
from django.utils import timezone
class seen_db(models.Model):
    studnt=models.ForeignKey(User,on_delete=models.CASCADE)
    time_zone=models.TimeField(default=timezone.now)
    seen=models.BooleanField(default=False)
class session_db(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    session_name=models.TextField()
    session=models.FileField()
    time_zone=models.TimeField(default=timezone.now)
    seen_db=models.ManyToManyField("seen_db",null=True,blank=True)
    akhtbar =models.ManyToManyField(akhtbar,null=True,blank=True)
class scientific_material_db(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    Image=models.FileField(null=True,blank=True)
    scientific_material_name=models.TextField()
    seen=models.ManyToManyField("seen_db",null=True,blank=True)
    session=models.ManyToManyField("session_db")