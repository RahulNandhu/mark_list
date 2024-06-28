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


def MarkList(request,p):

    if request.method=='POST':
        student=Students.objects.get(Sid=p)
        sem=request.POST['Semester']
        if sem:  # Check if semester is provided
            try:
                marks = Marks.objects.get(semester=sem, student=student)
                return render(request, 'marklist.html', {'marks': marks})
            except Marks.DoesNotExist:
                # Handle the case where the marks are not found
                return render(request, 'marklist.html', {'error': 'Marks not found for the selected semester.'})
        else:
            return render(request, 'marklist.html', {'error': 'Please select a semester.'})
    return render(request,template_name='marklist.html')