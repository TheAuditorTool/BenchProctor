// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

void benchmark_test_00324(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    char _dst[16];
    std::strcpy(_dst, data.c_str());
    std::cout << _dst << std::endl;
}
