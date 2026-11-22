// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00236(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char *_dst = new char[32];
    std::snprintf(_dst, 32, "user=%s", user_input.c_str());
    std::cout << _dst << std::endl;
    delete[] _dst;
}
