from django.shortcuts import render
from django.shortcuts import redirect	
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import Group
from Users.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def login(request):
	if request.method == "POST":
		origin = request.POST["origin"]
		email = request.POST['email']
		pwd = request.POST['pwd']
		user = authenticate(email= email, password= pwd)

		if user is not None and user.groups.filter(name=origin): 
			if user.groups.filter(name='Dealer').exists(): 
				auth_login(request, user)
				return HttpResponseRedirect(reverse('dealerHome', args=(user.referrelCode, )))

			if user.groups.filter(name='Influencer').exists(): 
				auth_login(request, user)
				return HttpResponseRedirect(reverse('home', args=(user.referrelCode, )))
			
			if user.groups.filter(name='Company').exists(): 
				auth_login(request, user)
				return HttpResponseRedirect(reverse('companyHome', args=(user.referrelCode, )))
		else:
			messages.error(request, "Invalid Login Credentials")
			return redirect('login')
	else:
		return render(request, 'Authentication/login.html')  


def signup(request): 
	if request.method == "POST": 
		origin = request.POST['origin']
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		pnumber = request.POST['pnumber']
		pwd = request.POST['pwd']
		repwd = request.POST['repwd']
		gstin = request.POST['gstin']
		referrel = request.POST['referrel']
		panNumber = request.POST['panNumber']
		panPhoto = request.POST.get('panPhoto')

		if pwd != repwd: 
			raise ValueError("Re-entered password does not match! ")
			return render(request, 'Authentication/signup.html')

		user = User.objects.create_user(email, repwd)
		user.first_name = fname
		user.last_name = lname 
		user.phoneNumber = pnumber 
		user.gstinNumber = gstin 
		user.referrelCode = referrel
		user.panNumber = panNumber
		user.panPhoto = panPhoto

		grp = Group.objects.get(name=origin)		
		grp.user_set.add(user)

		user.save() 
		return HttpResponse("<script>window.close();</script>")
		
	else:
		return render(request, 'Authentication/signup.html')



def logout(request):
	auth_logout(request)
	return redirect('login')	