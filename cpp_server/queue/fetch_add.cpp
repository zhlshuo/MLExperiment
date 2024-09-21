#include <atomic>
#include <iostream>
#include <vector>
#include <thread>

std::atomic<int> count;

void incrementWorker() {
    for(int i = 0; i < 1000; ++i) {
        count.fetch_add(1);
    }
}

int main() {
    std::vector<std::thread> threads;
    for(int i = 0; i < 10; ++i) {
        threads.push_back(std::thread(incrementWorker));
    }

    for(auto& t:threads){
        t.join();
    }

    std::cout << count << std::endl;

    std::cout << count.is_lock_free() << std::endl;
}