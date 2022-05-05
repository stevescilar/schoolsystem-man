from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models


# student model
# parents model
# classmodule
# subject model
# exam module
# Fee Module



class Student(models.Model):

    CLASS_NAMES = (
        ('PP1','PP1'),
        ('PP2','PP2'),
        ('Grade1','Grade1'),
        ('Grade2','Grade2'),
        ('Grade3','Grade3'),
        ('Grade4','Grade4'),
        ('Grade5','Grade5'),
        ('Grade6','Grade6'),
        ('Grade7','Grade7'),
        ('Grade8','Grade8'),
        # ('Grade7','Grade7'),
        # subject to increment
    )
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=GENDER, default='Male')
    parent_name = models.CharField(max_length=100)
    parent_contact = models.CharField(max_length=50)
    parent_email = models.EmailField(max_length=100, unique=True)
    class_name = models.CharField(max_length=10,choices=CLASS_NAMES, default='PP1')

    # required
    date_joined     = models.DateTimeField(auto_now_add = True)
    stud_pic = models.ImageField(upload_to = 'administration/students',blank=True)
    
    def full_name(self):
        return f'{self.first_name} {self.middle_name} {self.surname}'

    def __str__(self):
        return self.first_name
    
# class Finance(models.Model)