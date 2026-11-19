// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00005(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    size_t _n = data.size();
    int _mode;
    if (_n > 64) _mode = 2;
    else if (_n > 0) _mode = 1;
    std::cout << _mode << std::endl;
}
