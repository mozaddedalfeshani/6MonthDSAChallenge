#Min and Max in Array
class Solution:
    def get_min_max(self, arr):
        maxNumber =0
        minNumber=0 
        for item in arr:
            if(item>max):
                max = item
            if(item<min):
                min = item

        return maxNumber , minNumber
    

anObject= Solution
a , b= anObject.get_min_max([1,35,23,123,4342])

print(a,b)

