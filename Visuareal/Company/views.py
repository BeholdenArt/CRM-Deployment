from tokenize import group
from django.shortcuts import render, redirect
from Company.models import AddCustomer, CompanyInventory, OrderQueue, AddCompany
from Dealer.models import AddDealer
from Influencer.models import AddInfluencer
from django.http import JsonResponse
from django.http import HttpResponse
import json 
from django.core import serializers
from Users.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

from Points.models import ExtraPoints
from Dealer.models import DealerInventory
from Users.logic import Points

def companyHome(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			contents = AddCustomer.objects.filter(user = user).count()
			inventory = CompanyInventory.objects.filter(user = user).count()
			order = OrderQueue.objects.filter(user = user).count()
			context = {
				'customer' : contents,
				'inventory' : inventory,
				'order' : order,
				'url' : 'company', 
				'name' : "Company's",
				'extend' : "base.html" ,
				'user': user,
				'ref': ref,
			}
			return render(request, 'company/CompanyHome.html', context)
	else:
		return redirect('login')

def inventory_chart(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			labels = []
			data = []

			queryset = CompanyInventory.objects.filter(user=user).values('productName', 'productQuantity')
			for entry in queryset:
				labels.append(entry['productName'])
				data.append(entry['productQuantity'])
			
			return JsonResponse(data={
				'labels': labels,
				'data': data,
			})
	else:
		return redirect('login')

def orderQueue_chart(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			labels2 = []
			data2 = []
			q = OrderQueue.objects.all()
			print(q)
			queryset = OrderQueue.objects.values('orderedQuantity')
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


def companyCustomerList(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			contents = AddCustomer.objects.filter(user = user).all()
			context = {
				'all_data' : contents, 
				'extend' : 'base.html', 
				'url' : 'company', 
				'name' : "Company's",
				'user': user,
				'ref': ref,
			}
			return render(request, 'company/customerlist.html', context)
	else:
		return redirect('login')

def companyInventoryList(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			contents = CompanyInventory.objects.filter(user = user).all()
			context = {
				'all_data' : contents, 
				'extend' : 'base.html', 
				'url' : 'company', 
				'name' : "Company's",
				'user': user,
				'ref': ref,
			}	
			return render(request, 'company/inventorylist.html', context)
	else:
		return redirect('login')

def companyDealerList(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode= ref)
		if user is not None:
			contents = User.objects.filter(groups__name = 'Dealer')
			context = {
				'all_data' : contents, 
				'extend' : 'base.html',	
				'url' : 'company', 
				'name' : "Company's",
				'user': user,
				'ref': ref,
			}
			return render(request, 'company/dealerlist.html', context) 
	else:
		return redirect('login')	

def companyDeleteDealer(request, data_id, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			event = User.objects.get(pk=data_id)
			event.delete()
			return HttpResponseRedirect(reverse('companyDealerList', args=(ref, )))
	else:
		return redirect('login')

def companyInfluencerList(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			contents = User.objects.filter(groups__name = 'Influencer')
			context = {
				'all_data' : contents, 
				'extend' : 'base.html',
				'url' : 'company',
				'name' : "Company's", 
				'user': user,
				'ref': ref,
			}
			return render(request, 'company/influencerlist.html', context)
	else:
		return redirect('login')

def companyDeleteInfluencer(request, data_id, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			event = User.objects.get(pk=data_id)
			event.delete()
			return HttpResponseRedirect(reverse('companyInfluencerList', args=(ref, )))
	else:
		return redirect('login')


def companyOrderQueue(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			contents = OrderQueue.objects.all()
			context = {
				'all_data' : contents, 
				'extend' : 'base.html', 
				'url' : 'company', 
				'name' : "Company's",
				'user': user,
				'ref': ref,
			}
			return render(request, 'company/orderqueue.html', context)
	else:
		return redirect('login')

def companyAddInventory(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			if request.method == "POST":
				ProductName = request.POST.get("ProductName")
				ProductCategory = request.POST.get("ProductCategory")
				ProductQuantity = request.POST.get("ProductQuantity")
				Point = request.POST.get("Point")
				Price = request.POST.get("Price")
				# companyName = request.POST.get("CompanyName")
				# company = AddCompany.objects.filter(companyName__exact = companyName)
				# if ProductName in CompanyInventory.
				
				# print("-"*100, obj)
				# print("*"*100, obj.productQuantity)
				
				if CompanyInventory.objects.filter(productName__exact = ProductName).exists():
					obj = CompanyInventory.objects.filter(productName__exact = ProductName)[0]
					obj.productQuantity = int(obj.productQuantity) + int(ProductQuantity)
					print('obj.newQuantity: ', obj.productQuantity)
					obj.save()
					# obj = CompanyInventory.objects.get()
					# obj[0].save()

					
				else:
					obj = CompanyInventory(
						point = Point,
						price = Price, 
						productName = ProductName,
						productCategory = ProductCategory,
						productQuantity = ProductQuantity,
						user = user,

					)
					obj.save()
					ExtraPoints.objects.create(product = CompanyInventory.objects.filter(productName = ProductName)[0], user = user)

				
				return HttpResponse("<script>window.close();</script>")
			else:
				CompanyName = AddCompany.objects.all()
				context = {
					'CompanyName' : CompanyName,
					'extend' : 'popup.html',
				}
				return render(request, 'company/inventoryInsert.html', context)
		else:
			HttpResponse('not exists')
	else:
		return redirect('login')

def companyDeleteInventory(request, data_id, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			event = CompanyInventory.objects.filter(user = user).get(pk=data_id)
			event.delete()
			return HttpResponseRedirect(reverse('companyInventoryList', args=(ref, )))
			# return redirect('../inventoryList')
	else:
		return redirect('login')

def companyOrderQueueInsert(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			if request.method == "POST":
				PN = request.POST.get("ProductName")

				productSelected = CompanyInventory.objects.filter(productName = PN)[0]
				# OP = request.POST.get("OrderPlaced")
				# OT = request.POST.get("Companywhomordered")
				# OrderPlaced = User.objects.filter(groups__name = 'Dealer')
				# OrderTo = AddCompany.objects.filter(companyName__exact = OT)
				orderedQuantity = request.POST.get("orderedQuantity")
				Placedon = request.POST.get("Placedon")
				Expecteddeliveryon = request.POST.get("Expecteddeliveryon")
				obj = OrderQueue.objects.create(
					# orderFrom = user,
					# orderTo = OrderTo(0),
					user = user,
					orderedQuantity = orderedQuantity,
					placedOn = Placedon,
					expectedDelievery = Expecteddeliveryon,
					orderedProducts = productSelected,
				)
				# for pdt in productSelected:
				# 	obj.orderedProducts.add(pdt)

				print('--'*100, obj.orderedProducts, '--'*100)
				obj.save()
				print(obj)
				return HttpResponse("<script>window.close();</script>")

			else:
				ProductName = CompanyInventory.objects.all()
				OrderPlaced = User.objects.filter(groups__name = 'Dealer')
				print(OrderPlaced)
				OrderTo = AddCompany.objects.all()
				context = {
					'ProductName' : ProductName,
					'OrderPlaced' : OrderPlaced,
					'Companywhomordered' : OrderTo,
					'extend' : 'popup.html',
				}
				return render(request, 'company/orderQueueInsert.html', context)
	else:
		return redirect('login')

def companyDeleteOrderQueue(request, data_id, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			event = OrderQueue.objects.get(pk=data_id)
			event.delete()
			return HttpResponseRedirect(reverse('companyOrderQueue', args=(ref, )))
			# return redirect('../orderQueue')
	else:
		return redirect('login')

def companyapproveOrderQueue(request, data_id= '', ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			event = OrderQueue.objects.get(pk= data_id)
			print(event.orderedProducts)
			print(CompanyInventory.objects.filter(productName = event.orderedProducts).values('productCategory'))
			print(DealerInventory.objects.filter(productName__exact = event.orderedProducts))
			if DealerInventory.objects.filter(productName__exact = event.orderedProducts).exists():
				obj = DealerInventory.objects.filter(productName__exact = event.orderedProducts)[0]
				obj.productQuantity = int(obj.productQuantity) + int(event.orderedQuantity)
				print('obj.newQuantity: ', obj.productQuantity)
				obj.save()
			else:
				obj = DealerInventory.objects.create(
					user = event.user,
					productName = str(event.orderedProducts),
					productCategory = CompanyInventory.objects.filter(productName = event.orderedProducts).values_list('productCategory', flat=True)[0],
					productQuantity = event.orderedQuantity,
					price = CompanyInventory.objects.filter(productName = event.orderedProducts).values_list('price', flat=True)[0],
					point = CompanyInventory.objects.filter(productName = event.orderedProducts).values_list('point', flat=True)[0],
				)
				obj.save()
			Points(ref)
			quantity = CompanyInventory.objects.filter(productName__exact = event.orderedProducts).values_list('productQuantity')
			print("--"*10,quantity)
			if int(quantity[0][0]) >= event.orderedQuantity:
				new_quantity = (int(quantity[0][0]) - event.orderedQuantity)
				CompanyInventory.objects.filter(productName__exact = event.orderedProducts).update(productQuantity = new_quantity)
			
			companyDeleteOrderQueue(request, data_id, ref)

			return HttpResponseRedirect(reverse('companyOrderQueue', args=(ref, )))
			# return redirect('../orderQueue')
	else:
		return redirect('login')


def companyAddCustomer(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			if request.method == "POST": 
				name = request.POST.get("name")
				pnumber = request.POST.get("pnumber")
				influencedThrough = request.POST.get("influencedThrough")
				# interestedCompany = request.POST.get("interestedCompany")
				interestedPdt = request.POST.get("interestedProducts")
				dealerSuggested = request.POST.get("dealerSuggested")
				print('-'*100, influencedThrough, '-'*100)

				dealerName = User.objects.filter(email__exact = dealerSuggested)
				# companyInterested = AddCompany.objects.filter(companyName__exact = interestedCompany)
				influenced = User.objects.filter(email__exact = influencedThrough)
				productInterested = CompanyInventory.objects.filter(productName = interestedPdt)

				print('-'*100, influenced, '-'*100)
				# print('-'*100, influenced(0:1).get(), '-'*100)
				obj = AddCustomer.objects.create(
						user = user, 
						customerName= name, 
						customerPhoneNumber= pnumber, 
						influencedThrough= influenced[0],
						dealerName = dealerName[0],
						interestedProduct = productInterested[0],
						# companyInterested= companyInterested(0),
					)
				# for pdt in productInterested:
				# 	obj.interestedProduct.add(pdt)
				obj.save()
				return HttpResponse("<script>window.close();</script>")


			else:
				dealerList = User.objects.filter(groups__name = 'Dealer') 
				influencerList = User.objects.filter(groups__name = 'Influencer') 
				# companyList = AddCompany.objects.all() 
				companyInventory = CompanyInventory.objects.all()
				context = {
					'dealerList' : dealerList,
					'influencerList' : influencerList,
					# 'companyList' : companyList, 
					'companyInventory' : companyInventory, 
					'extend' : 'popup.html',  
				}
				return render(request, 'company/customerListInsert.html', context)
	else:
		return redirect('login')

def companyDeleteCustomer(request, data_id, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			event = AddCustomer.objects.filter(user =user).get(pk=data_id)
			event.delete()
			return HttpResponseRedirect(reverse('companyCustomerList', args=(ref, )))
			# return redirect('../customerList')
	else:
		return redirect('login')

def extraPoints(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			extra_points = ExtraPoints.objects.all()
			context = {
				'extra_points' : extra_points,
				'extend' : 'base.html', 
				'url' : 'company', 
				'name' : "Company's",
				'user': user,
				'ref': ref,
			}
			return render(request, 'table.html' , context)
	else:
		return redirect('login')

def updateExtraPoints(request,data_id, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			if request.method == "POST":
				festival = request.POST.get("festival")
				occasion = request.POST.get("occasion")
				misc = request.POST.get("misc")
				geography = request.POST.get("geography")
				print('-'*100, festival, occasion, misc, geography)
				obj = ExtraPoints.objects.get(pk=data_id)
				obj.festival = festival
				obj.occasion = occasion
				obj.misc = misc
				obj.geography = geography
				print(obj.festival, obj.occasion, obj.misc, obj.geography)
				obj.save()
				return HttpResponse("<script>window.close();</script>")

			else:
				contents = ExtraPoints.objects.get(pk=data_id)
				context = {
					'all_data': contents,
				}
				return render(request, 'updateExtraPoints.html', context)
	else:
		return redirect('login')

def companyDeleteCustomerAll(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			AddCustomer.objects.all().delete()
			return HttpResponseRedirect(reverse('companyCustomerList', args=(ref, )))
	else:
		return redirect('login')

def companyDeleteOrderQueueAll(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			OrderQueue.objects.all().delete()
			print("*"*10)
			return HttpResponseRedirect(reverse('companyOrderQueue', args=(ref, )))
	else:
		return redirect('login')

def companyDeleteInventoryAll(request, ref=''):
	if ref:
		user = User.objects.get(referrelCode = ref)
		if user is not None:
			CompanyInventory.objects.all().delete()
			return HttpResponseRedirect(reverse('companyInventoryList', args=(ref, )))
	else:
		return redirect('login')