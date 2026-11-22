// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <regex>

void benchmark_test_00249(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_ORIGIN");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    std::string arg = std::regex_match(data, std::regex("^(config|data|index|schema)$")) ? data : std::string("config");
    std::string _path = std::string("/var/app/data/") + arg;
    if (FILE *_f = std::fopen(_path.c_str(), "w")) std::fclose(_f);
}
