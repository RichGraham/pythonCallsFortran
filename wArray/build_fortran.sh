cd src_fortran
gfortran -fPIC -O3 -Wpedantic -Wall -Wextra -shared my_fortran_lib.f90 -o myflib.so
