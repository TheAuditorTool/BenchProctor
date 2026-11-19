// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00560(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_USER_AGENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::string _cmd = std::string("ls ") + data;
    std::system(_cmd.c_str());
}
