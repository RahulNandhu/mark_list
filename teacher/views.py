from django.shortcuts import render
from .models import Marks
from django.db.models import F, ExpressionWrapper, IntegerField


# Create your views here.

def Home(request):
    total_expression = (
            F('Language_1') + F('Language_2') + F('Maths') +
            F('Physics') + F('Chemistry') + F('Statistics') +
            F('Computer_Science')
    )

    Top_3 = Marks.objects.annotate(
        total_marks=ExpressionWrapper(total_expression, output_field=IntegerField())
    ).order_by('-total_marks')  # Sorted in descending order by total marks

    if len(Top_3)>3:
        Top_3=Top_3[3]

    context={'T3':Top_3}
    return render(request,template_name='Home.html',context=context)