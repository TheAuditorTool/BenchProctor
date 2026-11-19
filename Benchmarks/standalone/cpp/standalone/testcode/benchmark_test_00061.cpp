// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>

void benchmark_test_00061(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    char *_dst = new char[32];
    std::sprintf(_dst, "user=%s", data.c_str());
    std::cout << _dst << std::endl;
    delete[] _dst;
}
