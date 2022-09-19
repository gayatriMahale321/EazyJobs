from email import message
# from urllib import response
from django.http import response
from django.shortcuts import render
from django.contrib import messages
from home.forms import CompanyAuthForm, CompanyForm, JobOpeningForm, StudentForm,StudentAuthForm
from home.models import Company, JobOpening
from django.contrib.auth import authenticate,login,logout
from home.models import Student,JobOpening

# Create your views here.
def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'about.html')


def studentlogin(request):
    return render(request,'studentlogin.html')

def studentregistration(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Student Registered Successfully")
    else:
        fm=StudentForm()

    return render(request,'student_reg.html',{'form':fm})


def companyregistration(request):
    if request.method=="POST":
        fm=CompanyForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Company Registered Successfully")
    else:
        fm=CompanyForm()
    return render(request,'company_reg.html',{'form':fm})

def jobopenings(request):
    if request.method=="POST":
        fm=JobOpeningForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Opening Added Successfully")
    else:
        fm=JobOpeningForm()
    return render(request,'jobopening_reg.html',{'form':fm})


def joblisting(request):
 data=JobOpening.objects.all()
 details={'alldata':data}
 return render(request,'joblisting.html',details)

#   if not request.user.is_authenticated:  
#         if request.method=='POST':
#             id=request.POST.get('prname')
#             data=JobOpening.objects(openingfor=id)
#             details={'alldata':data}
#             return render(request,'joblisting.html',details)
#         else: 
#             data=JobOpening.objects.all()
#             details={'alldata':data}
#             return render(request,'joblisting.html',details)
    
#   else:
#         fm=StudentAuthForm()
#         return render(request,'studentlogin.html',{'form':fm})
def showjobfilter(request):
    if request.method=='POST':
        ar=request.POST.get('prname')
        print(ar)
        ob=JobOpening.objects.filter(openingfor__icontains=ar)

        #ob=jobopenings.objects.filter(openingfor__icontains=ar)
        details={'alldata':ob}
        return render(request,'joblisting.html',details)




def studentlogin(request):
          if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            try:
                ob=Student.objects.get(username=username,password=password)
                messages.success(request,"Login Successfull")
                return render(request,'studentprofile.html',{'uname':username})
            except Student.DoesNotExist:
                ob=None
                messages.warning(request,"username or password invalid")
                fm=StudentAuthForm()
                return render(request,'studentlogin.html',{'form':fm})    
          else:
            fm=StudentAuthForm()
            return render(request,'studentlogin.html',{'form':fm})
  

def studentprofile(request):
    return render(request,'studentprofile.html')

def user_logout(request):
    logout(request)
    return response.HttpResponseRedirect("/studentlogin")

def logoutcompany(request):
    logout(request)
    return response.HttpResponseRedirect("/companylogin")

def companylogin(request):
          if request.method=='POST':
            username=request.POST.get('cregno')
            email=request.POST.get('email')
            password=request.POST.get('password')
            try:
                ob=Company.objects.get(cregno=username,email=email,password=password)
                messages.success(request,"Login Successfull")
                return render(request,'companyprofile.html',{'uname':username})
            except Company.DoesNotExist:
                ob=None
                messages.warning(request,"username or password invalid")
                fm=CompanyAuthForm()
                return render(request,'comapanylogin.html',{'form':fm})    
          else:
            fm=CompanyAuthForm()
            return render(request,'companylogin.html',{'form':fm})

def companyprofile(request):
    return render(request,'companyprofile.html')
