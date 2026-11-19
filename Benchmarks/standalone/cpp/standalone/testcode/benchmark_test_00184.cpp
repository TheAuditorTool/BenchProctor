// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00184(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    delete[] _p;
    std::cout << _p << std::endl;
}
