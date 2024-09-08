from django.db import models
from django.forms import ModelForm
# Create your models here.

class Office(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
class Employee(models.Model):
    genders = [
        ('M','Male'),
        ('F','Female'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100,choices=genders)
    office = models.ForeignKey('Office',on_delete=models.CASCADE)

class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'