from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index, name='index'),
	path('login', auth_views.login, name='login'),
	path('logout', auth_views.logout, name='logout'),
	path('accounts/profile/', views.index, name="index"),
	path('accounts/profile/<int:id>', views.show, name="show")
]