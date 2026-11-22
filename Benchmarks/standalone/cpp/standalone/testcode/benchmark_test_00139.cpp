// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

void benchmark_test_00139(int, char **)
{
    const char *user_input_env = std::getenv("MULTIPART_FIELD");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::srand((unsigned)std::time(nullptr));
    int _token = std::rand();
    std::cout << "token for " << user_input << ": " << _token << std::endl;
}
