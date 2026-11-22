// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <regex>

void benchmark_test_00155(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    static const std::regex _re("^[a-zA-Z0-9 _.#~\\-]+$");
    std::string arg = std::regex_match(data, _re) ? data : std::string("default");
    std::string _path = std::string("/var/app/data/") + arg;
    std::remove(_path.c_str());
}
