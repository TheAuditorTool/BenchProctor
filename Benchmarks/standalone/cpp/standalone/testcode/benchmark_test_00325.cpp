// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00325(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    char _dst[16];
    size_t _n = user_input.size();
    std::memcpy(_dst, user_input.c_str(), _n + 1);
    std::cout << _dst << std::endl;
}
