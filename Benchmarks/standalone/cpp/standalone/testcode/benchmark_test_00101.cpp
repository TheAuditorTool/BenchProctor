// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00101(int, char **)
{
    const char *user_input_env = std::getenv("GRAPHQL_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    std::string _ckval = data;
    for (char &_c : _ckval) if (_c == '\r' || _c == '\n') _c = ' ';
    for (char &_c : _ckval) if (_c == '\r' || _c == '\n') _c = ' ';
    std::cout << "Set-Cookie: session=" << _ckval << "; Secure; HttpOnly; SameSite=Strict; Path=/\r\n";
}
