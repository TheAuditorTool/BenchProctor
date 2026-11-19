// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <regex>

void benchmark_test_00746(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    std::string safe = std::regex_match(data, std::regex("^(status|info|list|show)$")) ? data : std::string("status");
    execl("/bin/sh", "sh", "-c", safe.c_str(), (char *)nullptr);
}
