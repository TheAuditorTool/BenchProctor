// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00180(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    char *_dst = new char[16];
    std::strncpy(_dst, data.c_str(), 15);
    _dst[15] = '\0';
    delete[] _dst;
}
