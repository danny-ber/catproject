from django.db import models

# Create your models here.

class checking(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.IntegerField()
    role = models.CharField(max_length = 50)
    device_name = models.CharField(max_length = 50)
    device_type = models.CharField(max_length = 50)
    serial_number = models.CharField(max_length = 50)
    time_in = models.DateTimeField()

    def _str_(self):
        return self.first_name


class check_record(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.IntegerField()
    role = models.CharField(max_length = 50)
    device_name = models.CharField(max_length = 50)
    device_type = models.CharField(max_length = 50)
    serial_number = models.CharField(max_length = 50)
    time_in = models.CharField(max_length = 250)
    time_out = models.DateTimeField()

    def _str_(self):
        return self.first_name

class checker(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    phone = models.IntegerField()
    
    def _str_(self):
        return self.first_name