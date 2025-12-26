s=[1,1,1,0,1,1,1,1,1,1,0,1,1,0,1]
count=0
maxi=0
for num in s:
    if num== 1:
        count+=1
    else:
        if count>maxi:
            maxi=count
            count=0
if count>maxi:
    maxi=count
print(maxi)            
'''
output:6
'''
