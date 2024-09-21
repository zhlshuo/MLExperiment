#include <cstdint>
#include <string>

struct OptionPrice {
    // price
    double last; //80.53
    std::uint32_t last_size; //10
    std::string last_timestamp; //"2022-03-22T19:34:45.572+00:00"
    std::uint32_t volume; //11
    double ask; //81.2
    std::uint32_t ask_size; //127
    std::string ask_timestamp; //"2022-03-22T19:34:45.572+00:00"
    double bid; //80.65
    std::uint32_t bid_size; //127
    std::string bid_timestamp; //"2022-03-22T19:34:45.572+00:00"
    std::uint32_t open_interest; //8523
    std::string exercise_style; // "A" or "E"

    // stats
    double  implied_volatility; //0.53165
    double delta; //0.93722
    double gamma; //0.00151
    double theta; //0.01674
    double vega; //0.19026

    //option
    std::string code; //"AAPL230120C00090000"
    std::string ticker; //"AAPL"
    std::string expiration; //"2023-01-20"
    double strike; //90.0
    std::string type; //"call" or "put"
};