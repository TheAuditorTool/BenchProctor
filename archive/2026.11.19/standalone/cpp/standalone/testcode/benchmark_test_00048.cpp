// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00048(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    delete[] _p;
    std::cout << _p << std::endl;
}
