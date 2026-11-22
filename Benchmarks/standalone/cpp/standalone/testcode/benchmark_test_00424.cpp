// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

void benchmark_test_00424(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    char _first = _p[0];
    delete[] _p;
    std::cout << _first << std::endl;
}
