import ctypes as ct

# import the shared library
fortlib = ct.CDLL('src_fortran/myflib.so')

# Specify arguments and result types
fortlib.sum2.argtypes = [ct.POINTER(ct.c_double)]
fortlib.sum2.restype = ct.c_double

# Create a double and pass it to Fotran (by reference)
a = ct.c_double(5)
b = fortlib.sum2(ct.byref(a))
print(b)