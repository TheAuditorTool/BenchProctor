// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00547(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    const char _buf[16] = "fixedcontent12";
    int _i = std::atoi(user_input.c_str());
    if (_i >= 0 && _i < (int)sizeof(_buf)) std::cout << _buf[_i] << std::endl;
}
