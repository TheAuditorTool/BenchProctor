// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

void benchmark_test_00726(int, char **)
{
    const char *user_input_env = std::getenv("GRAPHQL_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::srand((unsigned)std::time(nullptr));
    int _token = std::rand();
    std::cout << "token for " << data << ": " << _token << std::endl;
}
