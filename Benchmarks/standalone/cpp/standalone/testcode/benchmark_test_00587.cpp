// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00587(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _dst[16];
    size_t _n = user_input.size();
    if (_n >= sizeof(_dst)) _n = sizeof(_dst) - 1;
    std::memcpy(_dst, user_input.c_str(), _n);
    _dst[_n] = '\0';
    std::cout << _dst << std::endl;
}
