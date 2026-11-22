// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <climits>

void benchmark_test_00255(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    std::string _joined = std::string("/var/app/data/") + data;
    char _resolved[PATH_MAX];
    if (!realpath(_joined.c_str(), _resolved)) return;
    if (std::string(_resolved).rfind("/var/app/data/", 0) != 0) return;
    std::string arg = _resolved;
    if (FILE *_f = std::fopen(arg.c_str(), "w")) std::fclose(_f);
}
