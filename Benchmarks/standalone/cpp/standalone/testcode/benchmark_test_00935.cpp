// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00935(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    const char _buf[16] = "fixedcontent12";
    int _i = std::atoi(data.c_str());
    std::cout << _buf[_i] << std::endl;
}
