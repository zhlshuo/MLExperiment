#include <iostream>
#include <cstdio>
#include <bitset>

int main() {
    int16_t n = 0;
    for(int i = 0; i < 15;++i){
        n |= 1<<i;
    }
    std::cout << n << std::endl;
    std::cout << std::bitset<16>(n) << std::endl;

    n = 1<<15;
    std::cout << n << std::endl;
    std::cout << std::bitset<16>(n) << std::endl;

    n |= 1;
    std::cout << n << std::endl;
    std::cout << std::bitset<16>(n) << std::endl;

    uint16_t un = 0;
    for(int i = 0; i < 16;++i){
        un |= 1<<i;
    }
    std::cout << un << std::endl;
    std::cout << std::bitset<16>(un) << std::endl;

    std::cout << 0x7fff << std::endl;
    std::cout << std::bitset<16>(0x7fff) << std::endl;
}