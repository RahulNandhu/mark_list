from django.shortcuts import render

# Create your views here.

def Search_student(request):

    if request.method=='POST':
        return render(request, template_name='student.html')
    return render(request,template_name='home.html')