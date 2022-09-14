from django.contrib import admin
from Influencer.models import AddInfluencer
# Register your models here.


# class AddInfluencerAdmin(admin.ModelAdmin):
# 	from Company.admin import AddCustomerInline
# 	inlines = [AddCustomerInline]
# 	model = AddInfluencer

# admin.site.register(AddInfluencer, AddInfluencerAdmin)

admin.site.register(AddInfluencer)