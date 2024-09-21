#include <iostream>
#include <mutex>
#include <string>
#include <thread>

std::mutex coutMutex;

int main() {
    std::thread t([]{
        std::cout << "Still waiting ..." << std::endl;
        std::lock_guard<std::mutex> lockGuard(coutMutex);
        std::cout << "child: " << std::this_thread::get_id() << std::endl;
    });

    std::lock_guard<std::mutex> lockGuard(coutMutex);
    std::cout << "creator: " << std::this_thread::get_id() << std::endl;
    t.join();
}