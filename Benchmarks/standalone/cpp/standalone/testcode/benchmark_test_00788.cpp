// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00788(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    const char _buf[16] = "fixedcontent12";
    int _i = std::atoi(user_input.c_str());
    std::cout << _buf[_i] << std::endl;
}
