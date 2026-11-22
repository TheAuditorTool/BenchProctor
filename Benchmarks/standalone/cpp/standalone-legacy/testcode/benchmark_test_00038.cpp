// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00038(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_USER_AGENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _ckval = user_input;
    for (char &_c : _ckval) if (_c == '\r' || _c == '\n') _c = ' ';
    for (char &_c : _ckval) if (_c == '\r' || _c == '\n') _c = ' ';
    std::cout << "Set-Cookie: session=" << _ckval << "; HttpOnly; SameSite=Strict; Path=/\r\n";
}
