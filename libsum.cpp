#include <iostream>
#include "libsum.h"

int main(){
    printf("bindings with ctypes\n");
    std::cout << "sum from c++: " <<  sum(5 ,6 ) << "\n";
    return sum(5,7);
}
