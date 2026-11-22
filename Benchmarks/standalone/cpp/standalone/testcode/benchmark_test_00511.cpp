// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00511(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _dst[16];
    size_t _n = user_input.size();
    std::memcpy(_dst, user_input.c_str(), _n + 1);
    std::cout << _dst << std::endl;
}
