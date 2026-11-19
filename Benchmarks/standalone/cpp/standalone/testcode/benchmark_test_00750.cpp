// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00750(int, char **)
{
    const char *user_input_env = std::getenv("MULTIPART_FIELD");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    const char *_found = std::strchr(data.c_str(), '=');
    std::cout << *_found << std::endl;
}
