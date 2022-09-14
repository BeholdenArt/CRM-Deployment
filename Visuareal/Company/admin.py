from django.contrib import admin
from Company.models import AddCustomer, CompanyInventory, AddCompany, OrderQueue

# class OrderQueueAdmin(admin.ModelAdmin):
# 	# readonly_fields= ('placedOn')
# 	def get_model_perms(self, request):
# 		return {} 

# class AddCustomerAdmin(admin.ModelAdmin):
# 	readonly_fields = ('createdOn', 'updatedOn')
# 	def get_model_perms(self, request):
# 		return {} 

# class CompanyInventoryAdmin(admin.ModelAdmin):
# 	def get_model_perms(self, request):
# 		return {} 

# class OrderQueueInline(admin.StackedInline):
# 	model = OrderQueue 
# 	extra = 0

# class AddCustomerInline(admin.StackedInline):
# 	model = AddCustomer
# 	extra = 0 

# class CompanyInventoryInline(admin.StackedInline):
# 	model = CompanyInventory
# 	extra = 0

# class AddCompanyAdmin(admin.ModelAdmin):
# 	inlines = [CompanyInventoryInline]
# 	model = AddCompany

# admin.site.register(OrderQueue, OrderQueueAdmin)
# admin.site.register(AddCustomer, AddCustomerAdmin)
# admin.site.register(CompanyInventory, CompanyInventoryAdmin)

admin.site.register(OrderQueue)
admin.site.register(AddCustomer)
admin.site.register(CompanyInventory)
admin.site.register(AddCompany)
# Register your models here.
