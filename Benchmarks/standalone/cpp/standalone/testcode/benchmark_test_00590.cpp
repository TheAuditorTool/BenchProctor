// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00590(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _ckval = user_input;
    std::printf("Set-Cookie: session=%s; Secure; HttpOnly; SameSite=Strict; Path=/\r\n", _ckval.c_str());
}
