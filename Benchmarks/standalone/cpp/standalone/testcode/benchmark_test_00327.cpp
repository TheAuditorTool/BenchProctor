// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00327(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_HOST");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _path = std::string("/var/app/data/") + user_input;
    std::remove(_path.c_str());
}
