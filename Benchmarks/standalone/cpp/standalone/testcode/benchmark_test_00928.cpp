// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00928(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    char *_dst = new char[16];
    size_t _n = user_input.size();
    std::memcpy(_dst, user_input.c_str(), _n + 1);
    std::cout << _dst << std::endl;
    delete[] _dst;
}
