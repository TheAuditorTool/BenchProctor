// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00532(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    char *_dst = new char[16];
    std::strncpy(_dst, data.c_str(), 15);
    _dst[15] = '\0';
    delete[] _dst;
}
