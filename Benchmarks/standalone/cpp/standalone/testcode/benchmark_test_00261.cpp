// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <fstream>
#include <regex>

void benchmark_test_00261(int, char **)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    static const std::regex _re("^[a-zA-Z0-9 _.#~\\-]+$");
    std::string arg = std::regex_match(user_input, _re) ? user_input : std::string("default");
    std::string _path = std::string("/var/app/data/") + arg;
    std::ifstream _in(_path);
    if (_in.is_open()) _in.close();
}
