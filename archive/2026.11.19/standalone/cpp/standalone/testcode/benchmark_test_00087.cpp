// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00087(int, char **)
{
    const char *user_input_env = std::getenv("GRAPHQL_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = cpp_own(user_input);
    std::string _path = std::string("/var/app/data/") + data;
    std::remove(_path.c_str());
}
