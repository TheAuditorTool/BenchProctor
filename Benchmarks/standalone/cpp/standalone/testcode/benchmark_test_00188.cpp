// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00188(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data = cpp_own(user_input);
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::cout << _p << std::endl;
    if (std::strchr(_p, ';') != nullptr) delete[] _p;
    delete[] _p;
}
