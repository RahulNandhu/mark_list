from django.urls import path
from . import views

app_name='student'

urlpatterns=[
    path('',views.Search_student,name="search_student"),
    path('student_mark/<int:p>',views.MarkList,name='Mark'),
]