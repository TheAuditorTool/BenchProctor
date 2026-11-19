// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00794(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    char *_dst = new char[16];
    size_t _n = data.size();
    if (_n > 15) _n = 15;
    std::memcpy(_dst, data.c_str(), _n);
    _dst[_n] = '\0';
    std::cout << _dst << std::endl;
    delete[] _dst;
}
