// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>
#include <fstream>

void benchmark_test_00256(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    std::string arg = std::string("/var/app/data/") + data.substr(data.find_last_of('/') + 1);
    std::ifstream _in(arg);
    if (_in.is_open()) _in.close();
}
