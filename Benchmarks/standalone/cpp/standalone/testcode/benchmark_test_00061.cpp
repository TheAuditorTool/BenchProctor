// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>
#include <fstream>
#include <regex>

void benchmark_test_00061(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    static const std::regex _re("^[a-zA-Z0-9 _.#~\\-]+$");
    std::string arg = std::regex_match(data, _re) ? data : std::string("default");
    std::string _path = std::string("/var/app/data/") + arg;
    std::ifstream _in(_path);
    if (_in.is_open()) _in.close();
}
