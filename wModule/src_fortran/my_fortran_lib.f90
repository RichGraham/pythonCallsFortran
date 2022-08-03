function sum2(a) result(b) bind(c, name='sum2')
  use iso_c_binding
  use myModule
  implicit none
  
    
  real(c_double), intent(in)  :: a
  real(c_double)              :: b

  b = a + additiveConstant
  
end function sum2

