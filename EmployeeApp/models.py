from django.db import models

# Create your models here.

class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=120)


class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=120)
    Department = models.CharField(max_length=120)
    DateOfJoining = models.DateField()
    PhotoFile = models.CharField(max_length=100)