#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr1=[10,20,30,40,50]
arr2=[2,4,5,8,10]
a=np.array(arr1)
b=np.array(arr2)
print("Original array")
print(a)
print(b)
print("\nVector addition")
print(a+b)
print("\nVector subtraction")
print(a-b)
print("\nVector multiplication")
print(a*b)
print("\nVector division")
print(a/b)
print("\nVector dot product")
print(a.dot(b))
print("\nScalar multipliation")
sclr=5
print("scalar value=",sclr)
def my_func(x,y):
    if x>y:
        return x-y
    else:
        return x+y
print("\n\nNumpy.vectorise method")
print("(Return x-y if x>y,otherwise return x+y)")
arr1=[10,4,20]
arr2=[2,3,30]
vec_func=np.vectorize(my_func)
print("array1:",arr1)
print("array2:",arr2)
print("result:",vec_func(arr1,arr2))


# In[ ]:




