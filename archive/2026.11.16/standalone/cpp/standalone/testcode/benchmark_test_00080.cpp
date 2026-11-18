// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00080(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_FORWARDED_FOR");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string _path = std::string("/var/app/data/") + data;
    std::remove(_path.c_str());
}
