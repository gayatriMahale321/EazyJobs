from tkinter.ttk import LabeledScale
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import Student,Company,JobOpening

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=['cregno','cname','cindustry','Phone','cadd','city','pincode','email','password']
        labels={'cregno':'Regd. No.','cname':'Company Name','cindustry':'Industry','cadd':'Address'}
        widgets = {'password': forms.PasswordInput()}
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['sname','mobile','sadd','city','pincode','email','domainknowledge','workexpinyears','username','password','cpassword']
        labels={'sname':'Student Name','sadd':'Address','domainknowledge':'Domain nowledge','workexpinyears':'Experience in Years','cpassword':'Confirm Password'}
        widgets = {'password': forms.PasswordInput()}
class JobOpeningForm(forms.ModelForm):
    class Meta:
        model=JobOpening
        fields=['cregno','openingfor','forfresher','expinyear','joblocation','ctc','details']
        Labels={'cregno':'Company Regd. No','openingfor':'Opening for Post','forfresher':'Freshers Allowed?','expinyear':'Experience in Years','joblocation':'Job Location','ctc':'Cost to Company','details':'Job Description'}

class StudentAuthForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['username','password']
        widgets = {'password': forms.PasswordInput()}

class CompanyAuthForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=['cregno','email','password']
        # labels={'cregno':'Regd. No.'}
        widgets={'password':forms.PasswordInput()}
       
        

