// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00387(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    char *_dst = new char[16];
    size_t _n = data.size();
    std::memcpy(_dst, data.c_str(), _n + 1);
    std::cout << _dst << std::endl;
    delete[] _dst;
}
