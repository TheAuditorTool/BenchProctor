// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00427(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _dst[16];
    if (user_input.size() < sizeof(_dst)) std::strcpy(_dst, user_input.c_str());
    else _dst[0] = '\0';
    std::cout << _dst << std::endl;
}
