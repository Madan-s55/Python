s=[100,1,4,7,2,10,6,8,-1]
fl=float('-inf')
sl=fl
for num in s:
    if num>fl:
        sl=fl
        fl=num
    elif num<fl and num>sl:
        sl=num
print(sl)
