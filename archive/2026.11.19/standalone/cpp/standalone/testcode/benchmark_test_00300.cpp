// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00300(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    const char *_found = std::strchr(data.c_str(), '=');
    if (_found) std::cout << *_found << std::endl;
}
