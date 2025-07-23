import datetime
import uuid

from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from viewflow.fields import CompositeKey


# Create your models here.


class Student(models.Model):
    # profilePicture = models.ImageField()
    genderChoices = [('M', 'Male'), ('F', 'Female')]

    cmsId = models.IntegerField(primary_key=True 
    )# validation 

    fullName = models.CharField( max_length=40)

    # cnicNumber = models.CharField(unique=True, max_length=16)

    #  validators=[MinLengthValidator(4)])

    phoneNumber = models.CharField(max_length=13, blank=True)

    gender = models.CharField(max_length=1, choices=genderChoices)

    guardianName = models.CharField(max_length=40)
    guardianPhoneNumber = models.CharField(max_length=13)

    permenantAddress = models.TextField()
    department = models.CharField(max_length=10)
    # hostelBlockName = models.ForeignKey('Hostel', on_delete=models.CASCADE)
    roomNumber = models.IntegerField(default=10)


    userAccount = models.ForeignKey(settings.AUTH_USER_MODEL,
     on_delete=models.CASCADE)

    def __str__(self):
         return self.fullName
     


class Manager(models.Model):
    genderChoices = [('M', 'Male'), ('F', 'Female')]
    # picture = models.ImageField()
    fullName = models.CharField(max_length=40, primary_key=True)

    phoneNumber = models.CharField(max_length=13)

    # gender = models.TextField()


    userAccount = models.ForeignKey(settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE)



    # cnicNumber = models.CharField(unique=True, max_length=16,
    #  validators=[MinLengthValidator(4)])

    # hostelBlockName = models.ForeignKey('Hostel', on_delete=models.CASCADE,blank=True)
    hostel = "GH1"

    emailAddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.fullName


class Hostel(models.Model):
    
    id  = CompositeKey(columns= ['hostelName', 'block'])

    hostelNameChoices = [
        ('gh', 'Ghazali'),
        ('rz', 'Razi'),
        ('rm', 'Rumi'),
        ('at', 'Attar'),
        ('hv', 'Hajveri'),
        ('zk', 'Zakaria'),
        ('ft', 'Fatima'),
        ('as', 'Ayesha'),
        ('am', 'Amna'),
        ('kj', 'Khadija'),
        ('zb', 'Zainab')
    ]
    # picture = models.ImageField()
    levelChoices = [('ug', 'UG'), ('pg', 'PG')]
    forGenderChoices = [('M', 'Male'), ('F', 'Female')]

    hostelName = models.CharField(max_length=2, choices=hostelNameChoices)
    level = models.CharField(max_length=2, choices=levelChoices)
    # managerName = models.ForeignKey('Manager', on_delete=models.CASCADE)

    def forGender(self):
        return 'M' if self.hostelName in ['Gh', 'Rz', 'Rm', 'At', 'Hv', 'Zk'] else 'F'

    block = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)], null=True)

    capacity = models.IntegerField(validators=[MaxValueValidator(600), MinValueValidator(1)])

    def __str__(self):
        return f"{self.hostelName}{self.block}"


class Room(models.Model):
    id = CompositeKey(columns = ['roomNumber','maxCapacity'])
    roomNumber = models.IntegerField(validators=[MaxValueValidator(450), MinValueValidator(101)])

    maxCapacity = models.IntegerField(validators= [MaxValueValidator(3), MinValueValidator(1)])

    noOfResidents = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(0)], default=0 )
    

    def __str__(self):
        return self.roomNumber


class Invoices(models.Model):
    typeChoices = [('MB', 'MessBill'), ('RB', 'RentBill')]
    id = CompositeKey(columns = ['hostelBlockName','monthName','billType'])
    # hostelBlockName = models.ForeignKey('Hostel', on_delete=models.CASCADE)
    hostelBlockName = models.CharField(max_length=15)
    monthName = models.CharField(max_length=15)
    billType = models.CharField(choices=typeChoices, max_length=2)
    invoiceFile = models.FileField(upload_to="../save_invoices/")


class room_change(models.Model):
    req_name = models.CharField(max_length=30, default='naam dydy bhai')
    req_room = models.IntegerField(default=10)
    with_name = models.CharField(max_length=30, default='naam dydy bhai')
    with_room = models.IntegerField(default=20)


class outPass(models.Model):
    id = CompositeKey(columns=['cmsId','From_date'])
    cmsId = models.IntegerField()
    From_date = models.DateField()
    To_date = models.DateField()
    reason = models.TextField()


class rProblems(models.Model):
    # image = models.ImageField()
    descrip = models.TextField()


class notice_board(models.Model):
    msg = models.TextField()
    d_time = models.DateTimeField(default=datetime.datetime.now)
    


class Attendance(models.Model):
    markingChoices = [('P','present'), ('A', 'absent')]
    
    id = CompositeKey(columns = ['date','student.cmsId'])

    date = models.DateField(default=datetime.date)
    marking = models.CharField(max_length=1, choices=markingChoices)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

