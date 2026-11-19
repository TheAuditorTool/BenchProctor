// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

void benchmark_test_00466(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    static const std::regex _re("^[a-zA-Z0-9 _.%\\-]+$");
    std::string safe = std::regex_match(data, _re) ? data : std::string("default");
    std::string _cmd = std::string("ls ") + safe;
    std::system(_cmd.c_str());
}
