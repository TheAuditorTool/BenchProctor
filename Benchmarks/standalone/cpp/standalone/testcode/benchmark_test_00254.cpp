// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00254(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    char _dst[16];
    size_t _n = data.size();
    std::memcpy(_dst, data.c_str(), _n + 1);
    std::cout << _dst << std::endl;
}
