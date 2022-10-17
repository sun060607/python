oddnumber = [1, 3, 5, 7, 9]
cafes = ['star', 'bene', 'yoger', 'friends']
A = [1, 5, 'A', 'CC', 'B']
listInList = [[1, 3, 5, 6, 7], cafes, oddnumber, 1, 3, 'Abc']

a = oddnumber[1:5]
b = cafes[1:]
c = A[:2]
d = listInList[0][1:4] #리스트 내 리스트 접근

print(a)
print(b)
print(c)
print(d)