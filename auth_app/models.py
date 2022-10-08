from django.db import models
from django.contrib.auth.models import User
class ansers(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    akhtbar_name=models.TextField(default="ادخل الاجابه هنا",)
    asner=models.BooleanField(default=False)
class akhtbar(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    so2al=models.TextField()
    akhtbar_name=models.TextField(default="name",)
    rate=models.BooleanField(default=False)
    anserrelated=models.ManyToManyField("ansers")
class prof_DB(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.FileField(null=True,blank=True)
    akhtbar=models.ManyToManyField("akhtbar")