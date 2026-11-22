// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00365(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::string _loc = data;
    for (char &_c : _loc) if (_c == '\r' || _c == '\n') _c = ' ';
    std::cout << "Location: " << _loc << std::endl;
}
