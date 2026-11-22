// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00478(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    char *_p = new char[16];
    std::strcpy(_p, "pending");
    std::cout << _p << std::endl;
    _p = new char[user_input.size() + 1];
    std::strcpy(_p, user_input.c_str());
    std::cout << _p << std::endl;
    delete[] _p;
}
