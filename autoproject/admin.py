from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Teacher
from .models import Student
from .models import Appointment
from django import forms

class StudentInline(admin.StackedInline):
	model = Student

class TeacherInline(admin.StackedInline):
	model = Teacher	

class UserAdmin(BaseUserAdmin):
	inlines = (StudentInline, TeacherInline)

class AppointmentForm(forms.ModelForm):
	student = forms.ModelChoiceField(queryset=Student.objects.filter(is_student=True))
	teacher = forms.ModelChoiceField(queryset=Teacher.objects.filter(is_teacher=True))

class AppointmentAdmin(admin.ModelAdmin):
	form = AppointmentForm	

# Register your models here.
admin.site.register(Appointment, AppointmentAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
