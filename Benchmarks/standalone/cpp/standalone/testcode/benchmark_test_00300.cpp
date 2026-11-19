// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00300(int, char **)
{
    const char *user_input_env = std::getenv("GRAPHQL_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::cout << "Location: " << data << std::endl;
}
