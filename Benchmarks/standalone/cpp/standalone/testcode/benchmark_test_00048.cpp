// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00048(int, char **)
{
    const char *user_input_env = std::getenv("GRAPHQL_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    const char *_sep = std::strstr(user_input.c_str(), "://");
    if (_sep) std::putchar(_sep[3]);
    std::putchar('\n');
}
