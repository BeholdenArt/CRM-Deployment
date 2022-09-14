from django.urls import path
from Company import views

urlpatterns = [
	# Home 
	path('<slug:ref>/', views.companyHome, name="companyHome"), 
	path('company-inventory-chart/<slug:ref>/', views.inventory_chart, name='company-inventory-chart'),
	path('company-orderQueue-chart/<slug:ref>/', views.orderQueue_chart, name='company-orderQueue-chart'),
	
	# Customer list
	path('companyCustomerList/<slug:ref>/', views.companyCustomerList, name="companyCustomerList"),
	path('companyAddCustomer/<slug:ref>/', views.companyAddCustomer, name='companyAddCustomer'),
	path('companyDeleteCustomer/<slug:ref>/<data_id>', views.companyDeleteCustomer, name="companyDeleteCustomer"),
	path('companyDeleteCustomerAll/<slug:ref>/', views.companyDeleteCustomerAll, name="companyDeleteCustomerAll"),
	
	# Influencer List
	path('companyInfluencerList/<slug:ref>/', views.companyInfluencerList, name="companyInfluencerList"), 
	path('companyDeleteInfluencer/<slug:ref>/<data_id>', views.companyDeleteInfluencer, name="companyDeleteInfluencer"), 

	# Dealer List	
	path('companyDealerList/<slug:ref>/', views.companyDealerList, name="companyDealerList"),  
	path('companyDeleteDealer/<slug:ref>/<data_id>', views.companyDeleteDealer, name="companyDeleteDealer"),
	
	# Inventory List
	path('companyInventoryList/<slug:ref>/', views.companyInventoryList, name="companyInventoryList"),
	path('companyAddInventory/<slug:ref>/', views.companyAddInventory, name='companyAddInventory'),
	path('companyDeleteInventory/<slug:ref>/<data_id>', views.companyDeleteInventory, name="companyDeleteInventory"),
	path('companyDeleteInventoryAll/<slug:ref>/', views.companyDeleteInventoryAll, name="companyDeleteInventoryAll"),

	# Order Queue
	path('companyOrderQueue/<slug:ref>/', views.companyOrderQueue, name="companyOrderQueue"),
	path('companyOrderQueueInsert/<slug:ref>/', views.companyOrderQueueInsert, name="companyOrderQueueInsert"),
	path('companyDeleteOrderQueue/<slug:ref>/<data_id>', views.companyDeleteOrderQueue, name="companyDeleteOrderQueue"),
	path('companyapproveOrderQueue/<slug:ref>/<data_id>', views.companyapproveOrderQueue, name="companyapproveOrderQueue"),
	path('companyDeleteOrderQueueAll/<slug:ref>/', views.companyDeleteOrderQueueAll, name="companyDeleteOrderQueueAll"),
	
	#Extra Points
	path('companyPoints/<slug:ref>/', views.extraPoints, name="companyPoints"),
	path('updatePoints/<slug:ref>/<data_id>', views.updateExtraPoints, name="updatePoints"),
	
]