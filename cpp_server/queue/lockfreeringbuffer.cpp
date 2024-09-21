#include <atomic>
#include <vector>
#include "../marketdata/option.cpp"

struct OptionPriceQueue {
    std::atomic<uint64_t> mIndex;
    std::atomic<uint64_t> mPendingIndex;
    std::vector<OptionPrice> mPrices;

    uint64_t capacity;
    OptionPriceQueue(uint64_t capacity): capacity(capacity) {
    }

    void push(OptionPrice& price) {
        
    }

    
};