// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>

void benchmark_test_00382(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    char _dst[32];
    std::snprintf(_dst, sizeof(_dst), "user=%s", data.c_str());
    std::cout << _dst << std::endl;
}
