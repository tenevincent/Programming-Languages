import numpy as np

 
"""
arr = np.array([1, 2, 3, 4, 5])
print(arr)


arr = np.array((1, 2, 3, 4, 5))
print(arr)


arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.shape)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(f'The array size is {arr.shape}. 2nd element on 1st dim: ', arr[0, 1])


arr = np.array(["data", 2, 3, 4])
print(arr)
print(arr.dtype)

"""




def copy_fcn():
    arr = np.array([1, 2, 3, 4, 5])
    xcopy = arr.copy()
    xcopy[0] = 0
    print(arr)
    print(xcopy)



def array_view():
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.view()
    arr[0] = 42
    print(arr)
    print(x)



arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)