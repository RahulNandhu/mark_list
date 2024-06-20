from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customuser(AbstractUser):
    phone = models.IntegerField(default=0)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Teacher(models.Model):
    Name=models.CharField(max_length=30)
    Tid=models.IntegerField(unique=True)
    Registerd=models.CharField(max_length=20,default='No')
    Registerd_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Students(models.Model):
    Name = models.CharField(max_length=30)
    Sid = models.IntegerField(unique=True)
    Registerd = models.CharField(max_length=20, default='No')
    Registerd_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Semester(models.Model):
    Semster_choices = (
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
        ('Semester 3', 'Semester 3'),
        ('Semester 4', 'Semester 4'),
        ('Semester 5', 'Semester 5'),
        ('Semester 6', 'Semester 6'),
    )

    name=models.CharField(max_length=30,choices=Semster_choices,unique=True)

    def __str__(self):
        return self.name


class Marks(models.Model):
    semester=models.ForeignKey(Semester,on_delete=models.CASCADE)
    student=models.ForeignKey(Students, on_delete=models.CASCADE)
    Language_1=models.IntegerField()
    Language_2=models.IntegerField()
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Chemistry=models.IntegerField()
    Statistics=models.IntegerField()
    Computer_Science=models.IntegerField()

    class Meta:
        unique_together = ('student','semester')

    def Total(self):
        return (self.Language_1 + self.Language_2 + self.Maths + self.Chemistry + self.Physics + self.Statistics + self.Computer_Science)

    def __str__(self):
        return f'{self.student.Name}_{self.semester.name}'