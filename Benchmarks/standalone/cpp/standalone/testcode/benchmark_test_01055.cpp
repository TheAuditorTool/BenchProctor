// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_01055(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_USER_AGENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    struct { int id; int flags; } _rec = { 0, 0 };
    _rec.id = std::atoi(user_input.c_str());
    std::cout << _rec.id << " " << _rec.flags << std::endl;
}
