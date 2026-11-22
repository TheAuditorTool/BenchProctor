// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <fstream>

void benchmark_test_00265(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_USER_AGENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    std::string arg = std::string("/var/app/data/") + data.substr(data.find_last_of('/') + 1);
    std::ifstream _in(arg);
    if (_in.is_open()) _in.close();
}
