// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <fstream>
#include <regex>

void benchmark_test_00135(int, char **)
{
    const char *user_input_env = std::getenv("USER_COMMENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    std::string arg = std::regex_match(data, std::regex("^(config|data|index|schema)$")) ? data : std::string("config");
    std::string _path = std::string("/var/app/data/") + arg;
    std::ifstream _in(_path);
    if (_in.is_open()) _in.close();
}
