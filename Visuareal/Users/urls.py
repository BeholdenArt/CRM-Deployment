from django.urls import path 
from Users import views

urlpatterns = [
	path('', views.login, name="login"), 
	path('signup/', views.signup, name="signup"), 
	path('logout/', views.logout, name='logout'), 
]