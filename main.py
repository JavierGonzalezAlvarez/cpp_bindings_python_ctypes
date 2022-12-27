import ctypes
import os
from typing import Self

class Calculations:
    """Class to calculate operations"""
    def sum(self, value_x: int, value_y: int) -> Self:
        """
            function sum
            path of the project
        """
        libname = 'libsum.so'
        library_from_cpp = ctypes.cdll.LoadLibrary(os.path.abspath(libname))
        char = 'RETURN FROM C++ (.cpp)'
        print(f'{char:-<50}')
        sum_from_cpp = library_from_cpp.main(value_x, value_y)
        char = 'RETURN FROM LIBSUM (library of c++)'
        print(f'{char:-<50}')
        print(sum_from_cpp)
        char = 'RETURN FROM PYTHON (sum)'
        print(f'{char:-<50}')
        print("sum from python 3.11 & parameters (values): ", value_x + value_y)
        return self

    def mult(self, value_x: int, value_y: int) -> Self:
        """function multiplication"""
        char = 'RETURN FROM PYTHON (multiplication)'
        print(f'{char:-<50}')
        print("multiplication from python 3.11 & parameters (values): ", value_x * value_y)
        return self
         

class Values(Calculations):
    """Class to send values"""
    def values(self, valuex, valuey) -> Self:
        """function values"""
        valuex = 8
        valuey = 2
        return valuex + valuey

if __name__ == "__main__":
    Values.sum(Values, 5, 15)
    Values.mult(Values, 5, 5)
    char = 'RETURN FROM PYTHON (class Values)'
    print(f'{char:-<50}')
    print("sum from python 3.11 & class: ", Values.values(Values, 8, 2))

"""
output:

RETURN FROM C++ (.cpp)----------------------------
bindings with ctypes
sum from c++: 11
RETURN FROM LIBSUM (library of c++)---------------
12
RETURN FROM PYTHON (sum)--------------------------
sum from python 3.11 & parameters (values):  20
RETURN FROM PYTHON (multiplication)---------------
multiplication from python 3.11 & parameters (values):  25
RETURN FROM PYTHON (class Values)-----------------
sum from python 3.11 & class:  10
"""
