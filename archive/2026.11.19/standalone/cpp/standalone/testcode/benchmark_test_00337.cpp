// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00337(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_USER_AGENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _ckval = user_input;
    std::printf("Set-Cookie: session=%s; HttpOnly; SameSite=Strict; Path=/\r\n", _ckval.c_str());
}
