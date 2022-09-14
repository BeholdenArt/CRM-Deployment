from django.shortcuts import render, redirect
from Company.models import AddCustomer, AddCompany, CompanyInventory
from Dealer.models import AddDealer
from Influencer.models import AddInfluencer
from django.http import HttpResponse
from Users.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from Users.logic import influencer_points
# Create your views here.

# def temp(request): 
# 	return HttpResponse('HELLOWORLD')
def home(request, ref=''):
	if ref: 
		user = User.objects.get(referrelCode= ref)
		if user is not None: 
			contents = AddCustomer.objects.all().filter(user=user).order_by('-id')[:5]
			customer = AddCustomer.objects.filter(user=user).count()
			cust = AddCustomer.objects.filter(user=user)
			dealer = cust.values('dealerName').distinct().count()
			points = user.totalPoints
			print('--'*10, dealer)
			context = {
				'customer': customer,
				'dealer' : dealer,
				'points' : points,
				'url' : "influencer",
				'user': user,
				'ref': ref,
				'all_data': contents,
				'extend' : "base.html",
			}
			return render(request, 'influencerhome.html', context)

	else:
		return redirect('login')
	# cont = AddCustomer.objects.count()
	# contents = AddCustomer.objects.all().order_by('-id')[:5]
	# context = {
	# 	'all_data' : contents,
	# 	'customer' : cont,
	# 	'url' : 'influencer',
	# 	'name': "Influencer's",
	# 	'extend' : "base.html"
	# }
	# return render(request, 'influencerhome.html', context)

def influencerCustomerList(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			contents = AddCustomer.objects.filter(user = user).all()
			if user is not None: 
					context = {
						'all_data' : contents,
						'url' : "influencer",
						'user': user,
						'ref': ref,
						'extend' : "base.html",
					}
					return render(request, 'influencer/customerlist.html' , context)
	else:
		return redirect('login')
	# context = {
	# 	'all_data' : contents, 
	# 	'extend' : 'base.html', 
	# 	'url' : "influencer", 
	# 	'name': "Influencer's",
	# }
	# return render(request, 'influencer/customerlist.html', context)

def influencerAddCustomer(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			if request.method == "POST": 
				name = request.POST["name"]
				pnumber = request.POST["pnumber"]
				interestedPdt = request.POST.get("interestedProducts")
				influencedThrough = request.POST.get("influencedThrough")
				# interestedCompany = request.POST.get("interestedCompany")
				dealerSuggested = request.POST.get("dealerSuggested")
				dealerName = User.objects.filter(email__exact = dealerSuggested)
				influencerName = User.objects.filter(email__exact = influencedThrough)
				# companyInterested = AddCompany.objects.filter(companyName__exact = interestedCompany)
				# influenced = AddInfluencer.objects.filter(influencerName__exact = influencedThrough)
				influenced = User.objects.get(referrelCode= ref)
				productInterested = CompanyInventory.objects.filter(productName = interestedPdt)[0]
				print("Hello",productInterested)
				obj = AddCustomer.objects.create(
						user= user,
						customerName= name, customerPhoneNumber= pnumber, 
						dealerName = dealerName[0],
						influencedThrough = influencerName[0], 
						interestedProduct = productInterested,
					)
				# for pdt in productInterested:
				# 	obj.interestedProduct.add(pdt)
				obj.save()
				influencer_points(ref)
				return HttpResponse("<script>window.close();</script>")


			else:
				dealerList = User.objects.filter(groups__name = 'Dealer')
				influencerList = User.objects.filter(groups__name = 'Influencer')
				# companyList = User.objects.all()
				companyInventory = CompanyInventory.objects.all()
				context = {
					'dealerList' : dealerList,
					'influencerList' : influencerList,
					# 'companyList' : companyList, 
					'companyInventory' : companyInventory, 
					'extend' : 'popup.html',  
				}
				return render(request, 'influencer/customerListInsert.html', context)
	else:
		redirect('login')

def deleteCustomer(request, data_id, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			event = AddCustomer.objects.get(pk=data_id)
			event.delete()
			return HttpResponseRedirect(reverse('influencerCustomerList', args=(ref, )))
			# return redirect('../customerList')
	else:
		redirect('login')