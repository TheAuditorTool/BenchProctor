// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <regex>

void benchmark_test_00084(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    std::string arg = std::regex_match(data, std::regex("^(status|info|list|show)$")) ? data : std::string("status");
    execl("/bin/sh", "sh", "-c", arg.c_str(), (char *)nullptr);
}
