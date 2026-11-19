// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00551(int, char **)
{
    const char *user_input_env = std::getenv("GRAPHQL_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    std::string _path = std::string("/var/app/data/") + data;
    std::remove(_path.c_str());
}
