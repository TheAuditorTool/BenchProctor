// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>

void benchmark_test_01025(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    char *_dst = new char[32];
    std::sprintf(_dst, "user=%s", data.c_str());
    std::cout << _dst << std::endl;
    delete[] _dst;
}
