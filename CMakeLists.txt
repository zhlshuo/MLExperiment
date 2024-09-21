cmake_minimum_required(VERSION 3.29)
project(waitfreeringbuffer VERSION 0.1.0 LANGUAGES C CXX)
add_executable(waitfreeringbuffer cpp_server/queue/compare_exchange_strong.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

find_package(benchmark REQUIRED)
target_link_libraries(waitfreeringbuffer benchmark::benchmark)