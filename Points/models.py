from django.db import models

# Create your models here.
class ExtraPoints(models.Model):
    user = models.ForeignKey('Users.User', on_delete= models.CASCADE)
    product = models.ForeignKey('Company.CompanyInventory', on_delete= models.CASCADE)
    festival = models.IntegerField(blank= True, null= True, default= 0)
    occasion = models.IntegerField(blank= True, null= True, default= 0)
    misc = models.IntegerField(blank= True, null= True, default= 0)
    geography = models.IntegerField(blank= True, null= True, default= 0)

    def __str__(self):
        return str(self.product)