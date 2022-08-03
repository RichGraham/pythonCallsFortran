import ctypes as ct
import numpy as np

# import the shared library
fortlib = ct.CDLL('src_fortran/myflib.so')
f = fortlib.double_array

# Specify arguments type as a pointer to double and two integers
f.argtypes=[ct.POINTER(ct.c_double), ct.POINTER(ct.c_double),ct.c_int, ct.c_int]

def callFunction(x):
    # Create a double array, pass it to Fortran as a pointer
    y = x.copy()
    x_ptr = x.ctypes.data_as(ct.POINTER(ct.c_double))
    y_ptr = y.ctypes.data_as(ct.POINTER(ct.c_double))

    # Call function
    rint = f(x_ptr, y_ptr, ct.c_int(x.shape[0]), ct.c_int(x.shape[1]))
    return y
