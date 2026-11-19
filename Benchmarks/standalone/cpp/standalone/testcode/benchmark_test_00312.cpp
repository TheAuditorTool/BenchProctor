// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>

void benchmark_test_00312(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    char *_dst = new char[32];
    std::sprintf(_dst, "user=%s", data.c_str());
    std::cout << _dst << std::endl;
    delete[] _dst;
}
