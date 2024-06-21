from .models import Semester
def Semester_links(request):
    s=Semester.objects.all()
    return {'sem':s}
