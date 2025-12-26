s={1,4,20,25,67}
for num in s:
    print(num,(hash(num)%len(s)))
'''
1 1
67 2
4 4
20 0
25 0
'''
