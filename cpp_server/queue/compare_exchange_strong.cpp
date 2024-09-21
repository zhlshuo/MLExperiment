#include <iostream>
#include <vector>
#include <thread>
#include <atomic>
#include <benchmark/benchmark.h>

int normalCount=0;
std::atomic<int> count;

void normalWorker() {
    for(int i = 0; i < 10000000; ++i){
        normalCount += 1;
    }
}

void lockFreeWorker() {
    int oldValue = count.load();
    for(int i = 0; i < 10000000; ++i) {
        while(!count.compare_exchange_strong(oldValue, oldValue+1));
    }
}

void waitFreeWorker() {
    for(int i = 0; i < 10000000; ++i) {
        count += 1;
    }
}

void normalThread(){
    // normal shared variable without lock, result will be wrong
    std::vector<std::thread> otherThreads;
    for(int i = 0; i < 10; ++i) {
        otherThreads.emplace_back(std::thread(normalWorker));
    }

    for(auto& t:otherThreads){
        t.join();
    }
    std::cout << normalCount << std::endl;
}

static void BM_normalThread(benchmark::State& state){
    for(auto _ : state) {
        normalThread();
    }
}
BENCHMARK(BM_normalThread);

void lockFreeThread(){
    // lock free worker using compare_exchange_strong
    std::vector<std::thread> threads;
    for(int i = 0; i < 10; ++i) {
        threads.emplace_back(std::thread(lockFreeWorker));
    }

    for(auto& t:threads){
        t.join();
    }
    std::cout << count << std::endl;
}
static void BM_lockFreeThread(benchmark::State& state){
    for(auto _ : state) {
        lockFreeThread();
    }
}
BENCHMARK(BM_lockFreeThread);

void waitFreeThread(){
    // wait free worker using atomic plus
    std::vector<std::thread> threads;
    for(int i = 0; i < 10; ++i) {
        threads.emplace_back(std::thread(waitFreeWorker));
    }

    for(auto& t:threads){
        t.join();
    }
    std::cout << count << std::endl;
}
static void BM_waitFreeThread(benchmark::State& state){
    for(auto _ : state) {
        waitFreeThread();
    }
}
BENCHMARK(BM_waitFreeThread);

BENCHMARK_MAIN();