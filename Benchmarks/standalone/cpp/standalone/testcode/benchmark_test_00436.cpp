// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00436(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    char _dst[16];
    size_t _n = data.size();
    if (_n >= sizeof(_dst)) _n = sizeof(_dst) - 1;
    std::memcpy(_dst, data.c_str(), _n);
    _dst[_n] = '\0';
    std::cout << _dst << std::endl;
}
