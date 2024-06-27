from django.shortcuts import render
from teacher.models import Marks,Students

# Create your views here.

def Search_student(request):

    if request.method=='POST':
        search_key=request.POST['search']

        if search_key !='':
            try:
                st=Students.objects.get(Sid=search_key)
                msg=''
            except:
                st=''
                msg='Enter Valid Student Id'
            return render(request, template_name='student.html',context={'msg':msg,'st':st})
        else:
            return render(request,template_name='student.html',context={'msg':'Enter Student Id'})
