// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00902(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data = cpp_own(user_input);
    char *_p = new char[16];
    std::strcpy(_p, "pending");
    std::cout << _p << std::endl;
    delete[] _p;
    _p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::cout << _p << std::endl;
    delete[] _p;
}
