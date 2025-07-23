from django import forms
from django.forms import ModelForm
from .models import Student

class profileForm(ModelForm):
    class Meta:
        model = Student
        fields = ('fullName', 'cmsId','phoneNumber',
        'department', 'roomNumber', 'guardianName',
        'guardianPhoneNumber','permenantAddress',
        )
