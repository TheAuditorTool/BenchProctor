// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>

void benchmark_test_00060(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    char _dst[32];
    std::sprintf(_dst, "user=%s", user_input.c_str());
    std::cout << _dst << std::endl;
}
