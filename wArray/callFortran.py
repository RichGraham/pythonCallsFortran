import ctypes as ct
import numpy as np

# import the shared library
fortlib = ct.CDLL('src_fortran/myflib.so')
f = fortlib.double_array

# Specify arguments type as a pointer to double and an integer
f.argtypes=[ct.POINTER(ct.c_double), ct.c_int]

def callFunction():
    # Create a double array, pass it to Fortran as a pointer
    x = np.ones((3,3), order="F")
    x_ptr = x.ctypes.data_as(ct.POINTER(ct.c_double))

    # Call function
    rint = f(x_ptr, ct.c_int(3))
    return x
