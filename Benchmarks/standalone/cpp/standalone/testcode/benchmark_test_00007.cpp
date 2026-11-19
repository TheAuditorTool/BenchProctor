// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

struct Payload { std::string value; };

void benchmark_test_00007(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_HOST");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    const char *_found = std::strchr(data.c_str(), '=');
    std::cout << *_found << std::endl;
}
