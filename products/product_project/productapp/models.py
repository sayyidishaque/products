from django.db import models


# Create your models here.
class fruits(models.Model):
    name = models.CharField(max_length=250)
    disc = models.CharField(max_length=250)
    rate = models.IntegerField()
    pic = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


#
#
class vegetables(models.Model):
    name = models.CharField(max_length=250)
    disc = models.CharField(max_length=250)
    rate = models.IntegerField()
    pic = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class kidsitem(models.Model):
    name = models.CharField(max_length=250)
    disc = models.CharField(max_length=250)
    rate = models.IntegerField()
    pic = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
