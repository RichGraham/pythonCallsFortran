subroutine double_array(x,y,N1,N2) bind(C, name="double_array")
    use iso_c_binding
    implicit none

    integer(c_int), intent(in), value   :: N1,N2
    real(c_double), intent(in)       :: x(N1,N2)
    real(c_double), intent(out)       :: y(N1,N2)

    y  = exp(x)

end subroutine double_array
