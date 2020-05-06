# A1 = [[1, 2, 3], [4, 5,6], [7,8,9]]
# B1 = [[col + 10 for col in row ] for row in A1]
# B_Result = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
# # Final Result : [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
# print(B1 == B_Result)
# A = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# B = [[3, 3, 3], [4, 4, 4], [5, 5, 5]]
# X= [[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(A, B)]
# X2 = [[3, 6, 9], [16, 20, 24], [35, 40, 45]]
# print(X == X2)
#FINAL RESULT [[3, 6, 9], [16, 20, 24], [35, 40, 45]]
# print(X)
# print(X is X2)
# print(id(X))
# print(id(X2))
"""
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)
x1 = 'minhdan'
x2 = 'minhdan'
print(x1 is x2)
#tim hieu ve zip 
#zip(*iterator)
# list_number = (1, 2, 3, 4)
# list_string = ['nam', 'hieu', 'toai', 'son']
# result = set(zip(list_number, list_string))
# print(result)
# Minh se tim hieu xem ZIP code ma nguon no nhu the nao 
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b)


#1 == khac voi IS
#  list duoc luu o ID khac voi string ...
"""


# Function MIn
# min_example = min(1, 2, 3)
# print(min_example)
# min_example2 = min('d', 'nam', 'anhdan')
# print(min_example2)
"""
Parameter : n1, n2, n3 one or more items to compare
iterable : an iterable, with one or more items to compare

"""


# Function ord 
#ord(charcater) function returns the number representing the unicode of specified character
# print(ord('a'))
# print(ord('A'))
#Function chr returns the character that represents the specified unicode
# print(chr(97))
# print(chr(65))
# print(chr(10000))
# print(chr('minhdan'))


#Function any() returns True if any item in an iterable are true, otherwise it returns False.
# my_list = [True, False, True]
# print(any(my_list))



# print(float('   -12345\t'))

# import copy
# a = [1, 2, ['CR7', 'Messi']]
# # b = copy.deepcopy(a)
# c = copy.copy(a)
# # print(id(a), id(b),id(c), id([10, 23, 56, [78]]))
# c[2].append('Cong Fuong')
# # print(b)
# print(a)

#  a = [1, 2, 3]
#  b = [1, 2, 3]
#  a.append('日本語')
#  a.append('English')
 # b = ?
# a = [1, 2, 3]
# b = a
# a.append('日本語')
# b.append('English')
# print(a, hex(id(a)))
# print(b, hex(id(b)))
#[1, 2, 3, '日本語', 'English'] 0x7fe6e5ab1f48
#[1, 2, 3, '日本語', 'English'] 0x7fe6e5ab1f48

# Minh phai hoc lai bo nho cua python thoi 
# unmutable inmutable 
# minhdan1= 'minhdan'
# minhdan2 = minhdan1

# print('minh dan',minhdan1 is minhdan2)
# print(id(minhdan1), id(minhdan2), id('minhdan'))
# minhdan1 = minhdan1 + 'nam'
# print(id(minhdan1), id(minhdan2))

# print(minhdan1)
# print(minhdan2)


# count = {}
# count[(1, 2, 4)] = 5
# count[(1, 2)] = 6
# count[(4, 2, 1)] =2
# tot =0
# for i in count:
#     tot += count[i]
# print(len(count) + tot)
# print(count, len(count)) #16

# total = {}
# def insert(items):
#     if items in total:
#         total[items] +=1
#     else:
#         total[items] =1
# insert('Hoc sinh')
# insert('Hoc sinh')
# insert('Sinh Vien')
# insert('Sinh Vien')
# insert('Giang Vien')

# print(len(total), total)
# dap an 3

# [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
# [[3, 6, 9], [16, 20, 24], [35, 40, 45]]
# chr()
# 12345.0
# rw
# re.compile.groupindex
# 3
# 16
# [10,23,56,[78]]
#5


# import numpy as np 
# a = np.array([[1,2,3],[0,1,4]])
# b = np.zeros((2,3), dtype=np.int16)
# print(b)
# c = np.ones((2,3), dtype = np.int16)
# print(c)
# d = a+b+c
# print(d)
# print(d[1,2])
#dap an 5

a = ['jose']
b = a
print(id(a), id(b))
# a: 0x7f280c89ef48  b: 0x7f280c89ef48
b[0] = 'jose mourinho'
print(id(a), id(b))
# a: 0x7f280c89ef48  b: 0x7f280c89ef48
print(a) # ['jose mourinho']
print(b) # ['jose mourinho']
# a = [1,2,4]
# b = [1,2,4]
# print(a is b)
# print( a == b)