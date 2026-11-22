// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00321(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    std::string _ckval = data;
    for (char &_c : _ckval) if (_c == '\r' || _c == '\n') _c = ' ';
    for (char &_c : _ckval) if (_c == '\r' || _c == '\n') _c = ' ';
    std::fputs((std::string("Set-Cookie: session=") + _ckval + "; Secure; HttpOnly; SameSite=Strict; Path=/\r\n").c_str(), stdout);
}
