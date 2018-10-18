from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Appointment
from .models import Student
from .models import User

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return redirect('login')
	if request.user.is_staff or request.user.is_superuser:
		return redirect('/admin/')
	else:
		if hasattr(request.user, 'student'):
			nbAppointments = Appointment.objects.filter(student_id=request.user.student.id).count()
			allAppointments = Appointment.objects.filter(student_id=request.user.student.id)
			return render(request, 'profile/student.html', {
				'nb': nbAppointments,
				'appointments': allAppointments,
				})
		elif hasattr(request.user, 'teacher'):	
			allAppointments = Appointment.objects.filter(teacher_id=request.user.teacher.id)
			allStudents = Student.objects.filter(is_student=True)
			return render(request, 'profile/teacher.html', {
				'appointments': allAppointments,
				'students': allStudents,
				})

def show(request, id):
	if not request.user.is_authenticated:
		return redirect('login')
	if request.user.is_staff or request.user.is_superuser:
		return redirect('/admin/')
	else:
		if id:
			user = User.objects.get(id=id)
			allAppointments = Appointment.objects.filter(teacher_id=request.user.teacher.id, student_id=user.student.id)
			return render(request, 'profile/studentProfile.html', {
				'student': user,
				'appointments': allAppointments,
				})
