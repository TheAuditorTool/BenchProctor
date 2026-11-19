// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00445(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    if (!user_input.empty()) data = user_input;
    char _dst[16];
    size_t _n = data.size();
    if (_n >= sizeof(_dst)) _n = sizeof(_dst) - 1;
    std::memcpy(_dst, data.c_str(), _n);
    _dst[_n] = '\0';
    std::cout << _dst << std::endl;
}
