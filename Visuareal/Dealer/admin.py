from django.contrib import admin
from Dealer.models import DealerInventory, AddDealer
# Register your models here.

# class DealerInventoryAdmin(admin.ModelAdmin):
# 	def get_model_perms(self, request):
# 		return {} 

# class DealerInventoryInline(admin.StackedInline):
# 	model = DealerInventory
# 	extra = 0 

# class AddDealerAdmin(admin.ModelAdmin):
# 	from Company.admin import AddCustomerInline
# 	inlines = [DealerInventoryInline, AddCustomerInline]
# 	model = AddDealer

# admin.site.register(DealerInventory, DealerInventoryAdmin)
admin.site.register(DealerInventory)

admin.site.register(AddDealer)