// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

void benchmark_test_00730(int, char **)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    static const std::regex _schema("^[a-zA-Z0-9 _.%\\-]+$");
    if (!std::regex_match(data, _schema)) return;
    std::string safe = data;
    std::string _cmd = std::string("ls ") + safe;
    std::system(_cmd.c_str());
}
