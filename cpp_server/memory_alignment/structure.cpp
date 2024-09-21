#include <iostream>

struct sample_struct1{
    bool flag;
    unsigned int timeout;
};

 struct sample_struct2{
    bool flag;
    unsigned int timeout;
} __attribute__((aligned(16)));

#pragma pack(2)
struct sample_struct_pragma{
    bool flag;
    unsigned int timeout;
};
#pragma pack()

struct sample_struct_aligned{
    bool flag;
    unsigned int timeout __attribute__((aligned(16)));
};

int main(){
    bool f;
    unsigned int t;
    sample_struct1 ss1;
    sample_struct2 ss2;
    sample_struct_pragma ssp;
    sample_struct_aligned ssa;

    std::cout << sizeof(f) << std::endl;
    std::cout << sizeof(t) << std::endl;
    std::cout << sizeof(ss1) << std::endl;
    std::cout << sizeof(ss2) << std::endl;
    std::cout << sizeof(ssp) << std::endl;
    std::cout << sizeof(ssa) << std::endl;

    void* p = nullptr;
    posix_memalign(&p, 16, 160);
    return 0;
}