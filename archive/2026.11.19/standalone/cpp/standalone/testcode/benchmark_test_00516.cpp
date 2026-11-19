// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00516(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = cpp_own(user_input);
    char *_dst = new char[16];
    std::strcpy(_dst, data.c_str());
    delete[] _dst;
}
