// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00331(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    size_t _n = data.size();
    char *_p = new char[_n + 1];
    std::memcpy(_p, data.c_str(), _n + 1);
    std::cout << _p << std::endl;
    std::memset(_p, 0, _n + 1);
    delete[] _p;
}
