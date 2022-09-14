from django.urls import path
from Influencer import views

urlpatterns = [

	# Home 
	path('<slug:ref>/', views.home, name="home"), 
	
	# Customer List 
	path('influencerCustomerList/<slug:ref>/', views.influencerCustomerList, name='influencerCustomerList'), 
	path('influencerAddCustomer/<slug:ref>/', views.influencerAddCustomer, name='influencerAddCustomer'),
	path('influencerDeleteCustomer/<slug:ref>/<data_id>', views.deleteCustomer, name="influencerDeleteCustomer"),
]