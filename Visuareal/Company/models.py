from django.db import models

# Create your models here.
class UserCredentials(models.Model):
	username = models.CharField(max_length= 30, verbose_name= "Username")
	email = models.EmailField(null= True, blank= True, verbose_name= "Email")
	password = models.CharField(max_length=20, verbose_name= "Password")

	class Meta: 
		abstract = True

class UserDocuments(models.Model):
	panNumber = models.CharField(max_length= 30, verbose_name= "Pan Number")
	panPhoto = models.ImageField(verbose_name= "Pan Photo")

	def __str__(self):
		return str(self.panNumber)

	class Meta: 
		abstract = True

class Inventory(models.Model):
	productName = models.CharField(max_length= 255, verbose_name= "Product Name")
	productCategory = models.CharField(max_length= 255, verbose_name= "Product Category")
	productQuantity = models.CharField(max_length= 255, verbose_name= "Product Quantity")
	price = models.IntegerField(verbose_name= "Product Price" , default=5000)
	point = models.IntegerField(default=5, verbose_name= "Product Ponits", blank=True, null=True)

	def __str__(self):
		return str(self.productName)

	class Meta: 
		abstract = True

# class Points(models.Model):
# 	totalPoint = models.IntegerField(default= 0, verbose_name= "Total Point")
# 	createdOn = models.DateTimeField(auto_now_add = True, verbose_name= "Created On")
# 	updatedOn = models.DateTimeField(auto_now= True, verbose_name= "Last Updated")

# 	def __str__(self):
# 		return str(self.totalPoint)

# 	class Meta: 
# 		abstract = True

class OrderQueue(models.Model):
	user = models.ForeignKey('Users.User', on_delete=models.CASCADE)
	orderedProducts = models.ForeignKey('Company.CompanyInventory', on_delete= models.CASCADE, verbose_name= "Order Placed", blank= True, null= True)
	orderedQuantity = models.IntegerField(default=10 , blank = True)
	placedOn = models.DateTimeField(blank= True, null= True)
	expectedDelievery = models.DateTimeField(blank= True, null= True)
	orderValue = models.BigIntegerField(default= 0, blank= True)
	# orderFrom = models.ForeignKey('Dealer.AddDealer', on_delete= models.CASCADE, verbose_name= "Dealer Who Ordered")
	# orderTo = models.ForeignKey('Company.AddCompany', on_delete= models.CASCADE, verbose_name= "Company Whom Ordered")

	def __str__(self):
		return str(self.user)

class AddCustomer(models.Model):
	user = models.ForeignKey('Users.User', on_delete=models.CASCADE, related_name= 'User')
	customerName = models.CharField(max_length= 30, verbose_name= "Customer Name")
	customerPhoneNumber = models.BigIntegerField(verbose_name= "Phone Number")
	interestedProduct = models.ForeignKey('Company.CompanyInventory', blank= True, null= True, verbose_name= "Interested Product", on_delete=models.CASCADE)
	# companyInterested = models.ForeignKey('Company.AddCompany', on_delete = models.CASCADE, blank= True, null= True, verbose_name= "Interested Company")
	influencedThrough = models.ForeignKey('Users.User', limit_choices_to={'groups__name': "Influencer"}, on_delete= models.CASCADE, blank= True, null= True, related_name= "InfluencerName")
	dealerName = models.ForeignKey('Users.User', limit_choices_to={'groups__name': "Dealer"}, on_delete= models.CASCADE, blank= True, null= True, related_name= "DealerName")
	createdOn = models.DateTimeField(auto_now_add= True, verbose_name= "Created On")
	updatedOn = models.DateTimeField(auto_now = True, verbose_name= "Last Updated")

	def __str__(self):
		return str(self.customerName)

class CompanyInventory(Inventory):
	user = models.ForeignKey('Users.User', on_delete=models.CASCADE)
	companyName = models.ForeignKey('Company.AddCompany', on_delete= models.CASCADE, blank= True, null= True)

class AddCompany(models.Model):
	user = models.ForeignKey('Users.User', on_delete=models.CASCADE)
	companyName = models.CharField(max_length= 30, verbose_name= "Company Name")
	dealerList = models.ManyToManyField('Dealer.AddDealer', blank= True, verbose_name= "Dealer List")
	influencerList = models.ManyToManyField('Influencer.AddInfluencer', blank= True, verbose_name= "Influencer List") 

	def __str__(self):
		return str(self.companyName)