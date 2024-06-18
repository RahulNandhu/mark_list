from django.contrib import admin
from .models import Customuser,Teacher,Students,Semester,Marks

# Register your models here.

admin.site.register(Customuser)
admin.site.register(Teacher)
admin.site.register(Students)
admin.site.register(Semester)
admin.site.register(Marks)




