// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00344(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    char _dst[16];
    if (data.size() < sizeof(_dst)) std::strcpy(_dst, data.c_str());
    else _dst[0] = '\0';
    std::cout << _dst << std::endl;
}
