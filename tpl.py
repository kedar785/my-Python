# 1
'''tpl=()
print(type(tpl),tpl)
x=(5,)
print(type(x))'''
 # 2
'''tpl=(4,5,6,7)
print(tpl[2])
print(tpl[-1])'''
 # 3
'''tpl=(3,6,2,7,11,85,[2,6,3])
tpl[-1][1]=90
print(tpl)'''

# 4
'''tpl=(2,4,7,6,9)
print(id(tpl))
tpl+=("hellp",5,7,8)
print(id(tpl))
print(tpl)'''
 # 5
'''tpl=(2,4,7,6,9)
del tpl
# print(tpl)'''

# 6
'''tpl=(2,4,1,23,7,6,91)
print(sorted(tpl,reverse=True))'''

# 7
'''tpl=(2,4,2,6,2,22,2,6)
print(tpl[0])
print(type(tpl))
print(tpl.count(2))'''

# 8
'''movies=[]
mov1=input("enter mov name")
mov2=input("entermov name")
mov3=input("enter mov name")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)'''

# 9
# palindrom
'''lst1=[2,4,2]
lst2=[2,8,3,6]
copyLst1=lst1.copy()
copyLst1.reverse()
if lst1==copyLst1:
    print("lst1 palindrom hai")
else :
    print("lst1 palindrom nhi hai")
copyLst2=lst2.copy()
copyLst2.reverse()
if lst2==copyLst2:
    print("lst2 palindrom hai")
else :
    print("lst2 palindrom nhi hai")'''

# 10
grade = ["A", "C", "A", "B", "A", "C", "D"]
'''r=grade.count("A")
print(r)'''
grade.sort()
print(grade)
