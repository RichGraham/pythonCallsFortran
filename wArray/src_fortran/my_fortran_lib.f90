subroutine double_array(x,N) bind(C, name="double_array")
    use iso_c_binding
    implicit none

    integer(c_int), intent(in), value   :: N
    real(c_double), intent(inout)       :: x(N,N)

    x  = exp(x)

end subroutine double_array
