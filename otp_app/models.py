# models.py
from django.db import models

class Student(models.Model):
    enrollment_no = models.CharField(max_length=20, unique=True)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.enrollment_no

class Device(models.Model):
    enrollment_no = models.OneToOneField(Student, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.device_id
