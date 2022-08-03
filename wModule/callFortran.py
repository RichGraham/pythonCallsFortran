import ctypes as ct

#====Initialise====
# import the shared library
fortlib = ct.CDLL('src_fortran/myflib.so')

# Specify arguments and result types
fortlib.sum2.argtypes = [ct.POINTER(ct.c_double)]
fortlib.sum2.restype = ct.c_double

def callFunction( inputArg):
    # Create a double and pass it to Fortran (by reference)
    a = ct.c_double(inputArg)
    return fortlib.sum2(ct.byref(a))