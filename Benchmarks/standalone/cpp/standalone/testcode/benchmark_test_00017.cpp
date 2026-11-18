// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00017(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_ORIGIN");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    std::cout << "Location: " << data << std::endl;
}
