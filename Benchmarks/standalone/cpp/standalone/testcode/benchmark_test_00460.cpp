// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00460(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    char *_dst = new char[16];
    std::strncpy(_dst, data.c_str(), 15);
    _dst[15] = '\0';
    delete[] _dst;
}
