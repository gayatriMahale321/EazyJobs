from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.index),
    path('contactus/',views.contactus,name='contact'),
    path('aboutus/',views.aboutus,name='about'),
    path('studentreg/',views.studentregistration,name='studentreg'),
    path('companyreg/',views.companyregistration,name='companyreg'),
    path('jobopening/',views.jobopenings,name='jobopening'),
    path('joblisting/',views.joblisting,name='joblisting'),
    path('joblistingpr/',views.showjobfilter,name='showjobfilter'),
    path('studentlogin/',views.studentlogin,name='studentlogin'),
    path('studentprofile/',views.studentprofile,name='studentprofile'),
    path('logout/',views.user_logout,name='logoutuser'),
    path('companylogin/',views.companylogin,name='companylogin'),
    path('companyprofile/',views.companyprofile,name='companyprofile'),
    path('companylogout',views.logoutcompany,name="logoutcompany"),
    
]