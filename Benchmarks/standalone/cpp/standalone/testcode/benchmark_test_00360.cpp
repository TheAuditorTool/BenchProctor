// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00360(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    size_t _n = user_input.size();
    int _mode;
    if (_n > 64) _mode = 2;
    else if (_n > 0) _mode = 1;
    else _mode = 0;
    std::cout << _mode << std::endl;
}
