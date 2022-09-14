from django.db import models
from Company.models import Inventory, UserDocuments, UserCredentials
# from Users.models import User
# Create your models here.


# Create your models here.

class DealerInventory(Inventory):
	user = models.ForeignKey('Users.User', on_delete=models.CASCADE)
	dealer = models.ForeignKey('Dealer.AddDealer', on_delete= models.CASCADE, blank= True, null= True)


class AddDealer(UserCredentials, UserDocuments):
	user = models.ForeignKey('Users.User', on_delete=models.CASCADE)
	dealerName = models.CharField(max_length= 255, verbose_name= "Dealer Name")
	referrelCode = models.CharField(max_length= 20, unique= True, verbose_name= "Referrel Code")
	UserDocuments._meta.get_field('panPhoto').upload_to = 'PanCard/Dealer/'
	
	def __str__(self):
		return str(self.dealerName)