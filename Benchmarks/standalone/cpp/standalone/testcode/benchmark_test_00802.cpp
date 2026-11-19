// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00802(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
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
    int _x;
    if (!data.empty()) _x = (int)data[0];
    std::cout << (_x + (int)data.size()) << std::endl;
}
