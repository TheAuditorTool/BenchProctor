// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <regex>

void benchmark_test_00518(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    static const std::regex _re("^[a-zA-Z0-9 _.%\\-]+$");
    std::string arg = std::regex_match(data, _re) ? data : std::string("default");
    execl("/bin/sh", "sh", "-c", arg.c_str(), (char *)nullptr);
}
