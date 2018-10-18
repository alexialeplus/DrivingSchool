from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField()
    paid_hours = models.IntegerField(default=0)

    def __str__(self):
        return self.student.username      


class Teacher(models.Model):	
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.teacher.username 

class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_appointment')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_appointment')
    date = models.DateTimeField()
    place = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        studentObject = User.objects.get(username=self.student)
        studentObject.student.paid_hours = int(studentObject.student.paid_hours) - 1
        studentObject.student.save()
        super(Appointment, self).save()

    def __str__(self):
        return "Rendez-vous du " + str(self.date) + " entre " + self.student.student.username + " et " + self.teacher.teacher.username

