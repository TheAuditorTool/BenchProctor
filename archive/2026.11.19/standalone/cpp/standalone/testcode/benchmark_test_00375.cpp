// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00375(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    char _dst[16];
    if (data.size() < sizeof(_dst)) std::strcpy(_dst, data.c_str());
    else _dst[0] = '\0';
    std::cout << _dst << std::endl;
}
