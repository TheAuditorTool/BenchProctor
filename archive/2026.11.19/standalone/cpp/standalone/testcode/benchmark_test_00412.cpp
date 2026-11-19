// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00412(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_HOST");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    std::string _ckval = data;
    std::printf("Set-Cookie: session=%s; HttpOnly; SameSite=Strict; Path=/\r\n", _ckval.c_str());
}
