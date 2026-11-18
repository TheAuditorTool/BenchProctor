// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00714(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    char _dst[16];
    if (data.size() < sizeof(_dst)) std::strcpy(_dst, data.c_str());
    else _dst[0] = '\0';
    std::cout << _dst << std::endl;
}
