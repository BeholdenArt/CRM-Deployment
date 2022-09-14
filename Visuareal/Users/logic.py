from math import floor
from Company.models import OrderQueue
from Users.models import User
from Company.models import CompanyInventory, AddCustomer
from Points.models import ExtraPoints

def Points(ref=''):
    if ref: 
        user = User.objects.get(referrelCode = ref)
        if user is not None:
            pdts = OrderQueue.objects.all()
            usr = pdts.last().user
            points = int(usr.totalPoints)

            pdt_quantity = pdts.last().orderedQuantity
            # pdt_quantity = OrderQueue.objects.filter(user= user).values('orderedQuantity')
            pdts = pdts.last().orderedProducts
            # print(pdts)
            # print('--'*10,pdts)
            # print(OrderQueue.objects.filter(user= user))
            pdt_points = list(CompanyInventory.objects.filter(productName = pdts).values_list('point', flat=True))
            print(pdt_points)
            ext_points = list(ExtraPoints.objects.filter(product = pdts).values_list('festival', 'occasion', 'misc', 'geography'))
            print(ext_points)
            print(sum(ext_points[0]) + sum(pdt_points))
            
            print(pdt_quantity)
            points += (sum(ext_points[0]) + sum(pdt_points))*pdt_quantity

            usr.totalPoints = points
            usr.save()

            # print(temp_sum)

def influencer_points(ref=''):
    if ref: 
        user = User.objects.get(referrelCode = ref)
        if user is not None:
            cust = AddCustomer.objects.all()
            usr = cust.last().user
            points = int(usr.totalPoints)
            print(cust.last().interestedProduct)
            intrested_pdt = cust.last().interestedProduct
            pdt_points = list(CompanyInventory.objects.filter(productName = intrested_pdt).values_list('point', flat=True))
            print(pdt_points)
            points += sum(pdt_points) + floor(0.30*sum(pdt_points))

            usr.totalPoints = points
            usr.save()
            



















    # if ref: 
    #     user = User.objects.get(referrelCode = ref)
    #     print(user.totalPoints)
    #     if user is not None:
    #         points = int(user.totalPoints)
            
    #         oq = list(OrderQueue.objects.values_list('orderValue'))
    #         temp_sum = sum(oq[0])
    #         print(temp_sum//20)
    #         print('-'*100, oq, '-'*100)
            
    #         if (temp_sum) <= 20000:
    #             points += 100
    #             # return points
    #         elif temp_sum <= 35000:
    #             points += 200
    #             # return points
    #         elif temp_sum <= 60000:
    #             points += 400
    #             # return points
    #         else :
    #             points += 600
    #             # return points
    #         print('Points----', points)
    #         # points.save()
    #         user.totalPoints = points 
    #         user.save() 
            