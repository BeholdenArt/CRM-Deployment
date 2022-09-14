from django.shortcuts import render, redirect
from Dealer.models import DealerInventory 
from Company.models import AddCustomer, OrderQueue, CompanyInventory, AddCompany
from Users.models import User
from Influencer.models import AddInfluencer
from django.shortcuts import redirect
from django.http import HttpResponse

from Dealer.models import AddDealer
from django.http import HttpResponse
import json 
from django.http import JsonResponse
from django.core import serializers
from json import dumps
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def dealerHome(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			contents = AddCustomer.objects.filter(user = user).count()
			inventory = DealerInventory.objects.filter(user = user).count()
			order = OrderQueue.objects.filter(user = user).count()
			context = {
				'customer' : contents,
				'inventory' : inventory,
				'order' : order,
				'points' : user.totalPoints,
				'ref' : ref,
				'extend': 'base.html', 
				'url' : "dealer", 
				'name': "Dealer's", 
			}
			return render(request, 'dealerhome.html', context)
	else:
		return redirect('login')

def inventory_chart(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			labels = []
			data = []

			queryset = DealerInventory.objects.filter(user=user).values('productName', 'productQuantity')
			for entry in queryset:
				print(entry['productName'])
				labels.append(entry['productName'])
				data.append(entry['productQuantity'])
			
			return JsonResponse(data={
				'labels': labels,
				'data': data,
			})


def orderQueue_chart(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			labels2 = []
			data2 = []
			q = OrderQueue.objects.filter(user=user).all()
			print(q)
			queryset = OrderQueue.objects.filter(user=user).values('orderedQuantity')
			print("hell", queryset)
			for i in q:
				labels2.append(i.orderedProducts.productName)
				print(labels2)
			for entry in queryset:
				data2.append(entry['orderedQuantity'])
			print(data2)
			print(labels2)
			return JsonResponse(data={
				'labels2': labels2,
				'data2': data2,
			})


def dealerCustomerList(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			contents = AddCustomer.objects.filter(user = user).all()
			context = {
				'all_data' : contents, 
				'extend' : 'base.html', 
				'url' : "dealer", 
				'name': "Dealer's",
				'ref' : ref,
			}
			return render(request, 'dealer/customerlist.html', context)
	else:
		return redirect('login')


def dealerInventoryList(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			contents = DealerInventory.objects.filter(user = user).all()
			context = {
				'all_data' : contents,
				'extend' : 'base.html', 
				'url' : "dealer", 
				'name': "Dealer's",
				'ref' : ref,
			}
			return render(request, 'dealer/inventorylist.html', context)
	else:
		return redirect('login')

def dealerOrderQueue(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			contents = OrderQueue.objects.filter(user = user).all()
			context = {
				'all_data' : contents, 
				'extend' : 'base.html', 
				'url' : "dealer", 
				'name': "Dealer's",
				'ref' : ref, 
			}
			return render(request, 'dealer/orderqueue.html', context)
	else:
		return redirect('login')

def dealerAddInventory(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			if request.method == "POST":
				ProductName = request.POST["ProductName"]
				ProductCategory = request.POST["ProductCategory"]
				ProductQuantity = request.POST["ProductQuantity"]
				# DName = request.POST.get("DealerName")
				# usr = User.objects.get(referrelCode= ref)
				obj = DealerInventory(
					productName = ProductName,
					productCategory = ProductCategory,
					productQuantity = ProductQuantity,
					user = user,
				)
				obj.save()
				return HttpResponse("windowClose.html")
			else:
				DealerName = AddDealer.objects.all()
				context = {
					'DealerName' : DealerName,
					'extend' : 'popup.html',
				}
				return render(request, 'dealer/inventoryInsert.html', context)

def dealerDeleteInventory(request, data_id, ref):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			event = DealerInventory.objects.filter(user = user).get(pk=data_id)
			event.delete()
			# return HttpResponseRedirect(reverse('inventoryList', args=(user.referrelCode, )))

			# return redirect ('../../inventoryList/ref')
			# return HttpResponseRedirect(reverse('inventoryList'), args=(ref, ))
			return HttpResponseRedirect(reverse('dealerInventoryList', args=(ref, )))

	else:
		return redirect('login')


def dealerOrderQueueInsert(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			if request.method == "POST":
				PN = request.POST.get("ProductName")
				productSelected = CompanyInventory.objects.filter(productName = PN)[0]
				Ov = CompanyInventory.objects.filter(productName = PN)
				Ov = list(Ov.values_list("price", flat=True))
				# OP = request.POST.get("OrderPlaced")
				# OT = request.POST.get("Companywhomordered")
				# OrderPlaced = User.objects.get(referrelCode= ref)
				# OrderPlaced = AddDealer.objects.filter(dealerName__exact = OP)
				# OrderTo = AddCompany.objects.filter(companyName__exact = OT)
				orderedQuantity = request.POST["orderedQuantity"]
				Ov = Ov[0]*int(orderedQuantity) 
				Placedon = request.POST["Placedon"]
				Expecteddeliveryon = request.POST["Expecteddeliveryon"]
				obj = OrderQueue.objects.create(
					user = user, 
					orderedQuantity = orderedQuantity,
					placedOn = Placedon,
					expectedDelievery = Expecteddeliveryon,
					orderValue = Ov,
					orderedProducts = productSelected,
					# orderFrom = OrderPlaced[0],
					# orderTo = OrderTo[0],
				)
				# for pdt in productSelected:
				# 	obj.orderedProducts.add(pdt)

				obj.save()
				print(obj)
				return HttpResponse("<script>window.close();</script>")

			else:
				ProductName = CompanyInventory.objects.all()
				OrderPlaced = AddDealer.objects.all()
				OrderTo = AddCompany.objects.all()
				context = {
					'ProductName' : ProductName,
					'OrderPlaced' : OrderPlaced,
					'Companywhomordered' : OrderTo,
					'extend' : 'popup.html',
				}
				return render(request, 'dealer/OrderQueueInsert.html', context)
	else:
		return redirect('login')

def dealerDeleteOrderQueue(request, data_id, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			event = OrderQueue.objects.filter(user = user).get(pk=data_id)
			event.delete()
			return HttpResponseRedirect(reverse('dealerOrderQueue', args=(ref, )))
			# return redirect('../orderQueue')
	else:
		return redirect('login')

def dealerAddCustomer(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			if request.method == "POST": 
				name = request.POST["name"]
				pnumber = request.POST["pnumber"]
				influencedThrough = request.POST.get("influencedThrough")
				interestedCompany = request.POST.get("interestedCompany")
				interestedPdt = request.POST.get("interestedProducts")
				dealerSuggested = request.POST.get("dealerSuggested")
				dealerName = User.objects.filter(email__exact = dealerSuggested)
				# companyInterested = User.objects.filter(email__exact = interestedCompany)
				influenced = User.objects.filter(email__exact = influencedThrough)
				productInterested = CompanyInventory.objects.filter(productName = interestedPdt)
				obj = AddCustomer.objects.create(
						customerName= name, customerPhoneNumber= pnumber, 
						influencedThrough= influenced[0],
						dealerName = dealerName[0],
						interestedProduct = productInterested[0],
						# companyInterested= companyInterested[0],
						user = user,
					)
				# for pdt in productInterested:
				# 	obj.interestedProduct.add(pdt)
				obj.save()
				return HttpResponse("<script>window.close();</script>")

			else:
				dealerList = User.objects.filter(groups__name = "Dealer") 
				influencerList = User.objects.filter(groups__name = "Influencer") 
				# companyList = User.objects.filter(groups__name = 'Company') 
				companyInventory = CompanyInventory.objects.all()
				context = {
					'dealerList' : dealerList,
					'influencerList' : influencerList,
					# 'companyList' : companyList, 
					'companyInventory' : companyInventory, 
					'extend' : 'popup.html',  
				}
				return render(request, 'dealer/customerListInsert.html', context)
	else:
		return redirect('login')

def dealerDeleteCustomer(request, data_id, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			event = AddCustomer.objects.filter(user = user).get(pk=data_id)
			event.delete()
			return HttpResponseRedirect(reverse('dealerCustomerList', args=(ref, )))
			# return redirect('../customerList')
	else:
		return redirect('login')

def dealerPoints(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			context = {
				'extend' : 'base.html', 
				'url' : "dealer", 
				'name' : "Dealer's",
				'user': user,
				'ref': ref,
			}
			return render(request, 'base.html' , context)