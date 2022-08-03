cd src_fortran
gfortran -O3 -fPIC -shared myModule.f90 my_fortran_lib.f90 -o myflib.so
