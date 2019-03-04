# xx
# map list

la = list('abcdef')
print(la)
# lb = [x[0] for x in la]
# print(lb)

def square(x):            # 计算平方数
     return x**2
M = map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
print(M)
print(list(M))  # [1, 4, 9, 16, 25]

lb = list(M)
sa = [x[0] for x in lb]
print(list(sa))
sb = [x[1] for x in lb]
print(sb)