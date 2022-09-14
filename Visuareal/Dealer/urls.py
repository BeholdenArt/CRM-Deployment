from django.urls import path
from Dealer import views

urlpatterns = [

	# Home 
	path('<slug:ref>/', views.dealerHome, name="dealerHome"), 
	path('inventory-chart/<slug:ref>/', views.inventory_chart, name='inventory-chart'),
	path('orderQueue-chart/<slug:ref>/', views.orderQueue_chart, name='orderQueue-chart'),
	
	# Customer List 
	path('dealerCustomerList/<slug:ref>/', views.dealerCustomerList, name="dealerCustomerList"),
	path('dealerAddCustomer/<slug:ref>/', views.dealerAddCustomer, name='dealerAddCustomer'),
	path('dealerDeleteCustomer/<slug:ref>/<data_id>', views.dealerDeleteCustomer, name="dealerDeleteCustomer"),
	
	# Inventory List 
	path('dealerInventoryList/<slug:ref>/', views.dealerInventoryList, name="dealerInventoryList"),
	path('dealerAddInventory/<slug:ref>/', views.dealerAddInventory, name='dealerAddInventory'),
	path('dealerDeleteInventory/<slug:ref>/<data_id>', views.dealerDeleteInventory, name="dealerDeleteInventory"),
	
	# Order Queue
	path('dealerOrderQueue/<slug:ref>/', views.dealerOrderQueue, name="dealerOrderQueue"),
	path('dealerOrderQueueInsert/<slug:ref>/', views.dealerOrderQueueInsert, name="dealerOrderQueueInsert"),
	path('dealerDeleteOrderQueue/<slug:ref>/<data_id>', views.dealerDeleteOrderQueue, name="dealerDeleteOrderQueue"),
	
	#Points
	path('dealerPoints/<slug:ref>/', views.dealerPoints, name="dealerPoints"),
]