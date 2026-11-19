// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00783(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    const char _buf[16] = "fixedcontent12";
    int _i = std::atoi(data.c_str());
    if (_i >= 0 && _i < (int)sizeof(_buf)) std::cout << _buf[_i] << std::endl;
}
