from django.shortcuts import render
from .models import Marks,Semester
from django.db.models import F, ExpressionWrapper, IntegerField,Sum


# Create your views here.

def Home(request):
    total_expression = (
            F('Language_1') + F('Language_2') + F('Maths') +
            F('Physics') + F('Chemistry') + F('Statistics') +
            F('Computer_Science')
    )

    semester=Semester.objects.get(name='Semester 1')
    mark_queryset = Marks.objects.filter(semester=semester)

    annotated_marks = mark_queryset.annotate(
        total_marks=ExpressionWrapper(total_expression, output_field=IntegerField())
    )

    # Aggregate and sort by total_marks for each student and semester
    Top = (
        annotated_marks.values('student__id', 'student__Name', 'semester__id', 'semester__name')
            .annotate(total_marks=Sum('total_marks'))
            .order_by('-total_marks')
    )

    # Top 3 students in Maths
    maths = (
        annotated_marks.values('student__id', 'student__Name', 'semester__id', 'semester__name')
            .annotate(total_marks=Sum('Maths'))
            .order_by('-total_marks')
    )

    # Top 3 students in Physics
    physics = (
        annotated_marks.values('student__id', 'student__Name', 'semester__id', 'semester__name')
            .annotate(total_marks=Sum('Physics'))
            .order_by('-total_marks')
    )



    if request.method=='POST':
        sem=request.POST['Sem']
        # print(sem)
        semester=Semester.objects.get(id=sem)
        mark_queryset=Marks.objects.filter(semester=semester)

        annotated_marks = mark_queryset.annotate(
            total_marks=ExpressionWrapper(total_expression, output_field=IntegerField())
        )

        # Aggregate and sort by total_marks for each student and semester
        Top = (
            annotated_marks.values('student__id', 'student__Name', 'semester__id', 'semester__name')
                .annotate(total_marks=Sum('total_marks'))
                .order_by('-total_marks')
        )

        # Top 3 students in Maths
        maths = (
            annotated_marks.values('student__id', 'student__Name', 'semester__id', 'semester__name')
                .annotate(total_marks=Sum('Maths'))
                .order_by('-total_marks')
        )

        # Top 3 students in Physics
        physics = (
            annotated_marks.values('student__id', 'student__Name', 'semester__id', 'semester__name')
                .annotate(total_marks=Sum('Physics'))
                .order_by('-total_marks')
        )

        context = {
            'T3': Top,
            'Maths': maths,
            'Physics': physics,
            'semester':semester
        }

        return render(request, 'Home.html', context)

    context={'T3':Top,'Maths':maths,'Physics':physics,'semester':'Semester 1'}
    return render(request,template_name='Home.html',context=context)