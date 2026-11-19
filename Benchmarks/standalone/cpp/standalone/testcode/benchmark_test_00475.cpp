// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00475(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char *_p = new char[user_input.size() + 1];
    std::strcpy(_p, user_input.c_str());
    if (std::strchr(_p, ';') != nullptr) { delete[] _p; return; }
    std::cout << _p << std::endl;
    delete[] _p;
}
