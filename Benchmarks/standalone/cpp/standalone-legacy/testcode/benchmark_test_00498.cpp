// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00498(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    size_t _n = user_input.size();
    char *_p = new char[_n + 1];
    std::memcpy(_p, user_input.c_str(), _n + 1);
    std::cout << _p << std::endl;
    delete[] _p;
    std::memset(_p, 0, _n + 1);
}
