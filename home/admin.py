from django.contrib import admin
from home.models import Company, JobOpening, contactus,Student
# Register your models here.
admin.site.register(contactus)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(JobOpening)
