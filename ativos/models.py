import datetime

from django.db import models


# Create your models here.


class Software(models.Model):
    arch = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    guid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    install_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.name}: {self.version}"

class Computer(models.Model):
    device_uid = models.CharField(unique=True, max_length=255, null=True)
    softwares = models.ManyToManyField(Software)

    def __str__(self):
        return self.device_uid