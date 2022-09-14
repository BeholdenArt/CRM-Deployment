from Company.models import OrderQueue
from Users.models import User

def Points(ref=''):
    if ref: 
        user = User.objects.get(referrelCode = ref)
        print(user.totalPoints)
        if user is not None:
            points = int(user.totalPoints)
            
            oq = list(OrderQueue.objects.values_list('orderValue'))
            temp_sum = sum(oq[0])
            print(temp_sum//20)
            print('-'*100, oq, '-'*100)
            
            if (temp_sum) <= 20000:
                points += 100
                # return points
            elif temp_sum <= 35000:
                points += 200
                # return points
            elif temp_sum <= 60000:
                points += 400
                # return points
            else :
                points += 600
                # return points
            print('Points----', points)
            # points.save()
            user.totalPoints = points 
            user.save() 
            