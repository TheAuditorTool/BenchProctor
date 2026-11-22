// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00042(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    if (std::strchr(_p, ';') != nullptr) return;
    std::cout << _p << std::endl;
    delete[] _p;
}
