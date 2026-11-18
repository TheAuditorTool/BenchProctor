// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00123(int, char **)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    std::cout << "Location: " << data << std::endl;
}
