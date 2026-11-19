// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00478(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    delete[] _p;
    std::cout << _p << std::endl;
}
