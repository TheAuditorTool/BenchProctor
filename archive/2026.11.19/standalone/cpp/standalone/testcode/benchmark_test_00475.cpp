// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

struct Payload { std::string value; };

void benchmark_test_00475(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    std::string _ckval = data;
    std::printf("Set-Cookie: session=%s; Secure; HttpOnly; SameSite=Strict; Path=/\r\n", _ckval.c_str());
}
