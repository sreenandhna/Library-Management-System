from datetime import timedelta
from django.contrib.auth.models import User
from django.db import models
from _datetime import datetime,timedelta


# Create your models here.
class adminsignupmodel(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    firstname=models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250,unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Newbookmodel(models.Model):
    CATEGORY_CHOICES = (
        ('al', 'Algorithms'),
        ('ai', 'Artificial Intelligence'),
        ('ml', 'Machine Learning'),
        ('pro', 'Programming'),
        ('net', 'Networking'),
        ('hr', 'Hardware'),
    )
    bookname = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    year = models.PositiveIntegerField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    shelfid = models.FloatField(default=None,null=True,blank=True)
    publisher = models.CharField(max_length=250)


    def __str__(self):
        return f"{self.bookname} {self.author}"


class studentsignupmodel(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    BRANCH_CHOICES = (
        ('CS', 'Computer Science'),
        ('AI', 'Artificial Intelligence'),
        ('ML', 'Machine Learning'),
        ('M.Tech', 'Image Processing'),
    )
    firstname=models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250,unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    branch = models.CharField(max_length=6, choices=BRANCH_CHOICES)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


def get_expiry():
    return datetime.today() + timedelta(days=15)

class IssuedBook(models.Model):
    #moved this in forms.py
    #enrollment=[(student.enrollment,str(student.get_name)+' ['+str(student.enrollment)+']') for student in StudentExtra.objects.all()]
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Newbookmodel, on_delete=models.CASCADE, null=True, blank=True)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
