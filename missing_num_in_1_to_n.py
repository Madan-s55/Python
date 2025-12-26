s=[1,2,4,5,6,7,8,9]
def helper(s):
    
    for i in range(1,len(s)+1):
        if i!=s[i-1]:
            return i
    return "No missing number"
print(helper(s))
'''
3
'''
