// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00854(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_AUTHORIZATION");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    std::cout << "Location: " << data << std::endl;
}
