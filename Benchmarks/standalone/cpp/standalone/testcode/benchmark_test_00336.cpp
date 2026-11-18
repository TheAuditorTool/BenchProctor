// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <climits>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00336(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = cpp_own(user_input);
    std::string _joined = std::string("/var/app/data/") + data;
    char _resolved[PATH_MAX];
    if (!realpath(_joined.c_str(), _resolved)) return;
    if (std::string(_resolved).rfind("/var/app/data/", 0) != 0) return;
    std::string safe = _resolved;
    std::remove(safe.c_str());
}
