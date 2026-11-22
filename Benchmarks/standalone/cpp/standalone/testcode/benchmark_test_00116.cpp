// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

void benchmark_test_00116(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    char _dst[16];
    size_t _n = data.size();
    std::memcpy(_dst, data.c_str(), _n + 1);
    std::cout << _dst << std::endl;
}
