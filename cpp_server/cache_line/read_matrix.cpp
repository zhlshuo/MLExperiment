#include <iostream>
#include <chrono>

using namespace std::chrono;


int main(){
    const int row = 100, col = 32 * 1024;
    char matrix[row][col];
    for(int i = 0; i < row; ++i){
        for(int j = 0; j < col; ++j){
            matrix[i][j] = 'c';
        }
    }

    auto start = high_resolution_clock::now();
    for(int i = 0; i < row; ++i){
        for(int j = 0; j < col; ++j){
            matrix[i][j] += 1;
        }
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    std::cout << duration.count() << " ms" << std::endl;

    start = high_resolution_clock::now();
    for(int j = 0; j < col; ++j){
        for(int i = 0; i < row; ++i){
            matrix[i][j] += 1;
        }
    }
    stop = high_resolution_clock::now();
    duration = duration_cast<microseconds>(stop - start);
    std::cout << duration.count() << " ms" << std::endl;

    return 0;
}