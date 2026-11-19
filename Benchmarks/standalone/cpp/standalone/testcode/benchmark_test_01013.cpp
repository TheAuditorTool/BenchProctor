// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_01013(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    size_t _n = data.size();
    char *_p = new char[_n + 1];
    std::memcpy(_p, data.c_str(), _n + 1);
    std::cout << _p << std::endl;
    delete[] _p;
    std::memset(_p, 0, _n + 1);
}
