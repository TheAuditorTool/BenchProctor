// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

struct Payload { std::string value; };

void benchmark_test_00371(int, char **)
{
    const char *user_input_env = std::getenv("USER_COMMENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    std::string _loc = data;
    for (char &_c : _loc) if (_c == '\r' || _c == '\n') _c = ' ';
    std::fprintf(stdout, "Status: 302 Found\r\nLocation: %s\r\n\r\n", _loc.c_str());
}
