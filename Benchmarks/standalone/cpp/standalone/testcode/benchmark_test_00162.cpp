// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00162(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    char *_p = new char[16];
    std::strcpy(_p, "pending");
    std::cout << _p << std::endl;
    delete[] _p;
    _p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::cout << _p << std::endl;
    delete[] _p;
}
