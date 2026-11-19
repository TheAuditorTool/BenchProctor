// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <climits>

void benchmark_test_00626(int, char **)
{
    const char *user_input_env = std::getenv("USER_COMMENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::string _joined = std::string("/var/app/data/") + data;
    char _resolved[PATH_MAX];
    if (!realpath(_joined.c_str(), _resolved)) return;
    if (std::string(_resolved).rfind("/var/app/data/", 0) != 0) return;
    std::string safe = _resolved;
    if (FILE *_f = std::fopen(safe.c_str(), "r")) std::fclose(_f);
}
