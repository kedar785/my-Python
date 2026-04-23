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
tpl=(2,4,1,23,7,6,91)
print(sorted(tpl,reverse=True))