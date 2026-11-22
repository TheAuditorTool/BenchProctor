// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00057(int, char **)
{
    const char *user_input_env = std::getenv("PATH_INFO");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _dst[32];
    std::snprintf(_dst, sizeof(_dst), "user=%s", user_input.c_str());
    std::cout << _dst << std::endl;
}
