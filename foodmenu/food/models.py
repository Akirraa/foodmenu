from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.s
class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1) # type: ignore
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://th.bing.com/th/id/OIP.CAXQe3AgWFel1hIzxDZ6owEsDg?w=266&h=199&c=7&r=0&o=5&dpr=1.3&pid=1.7")


    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})