// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>
#include <regex>

void benchmark_test_00031(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    std::string arg = std::regex_match(data, std::regex("^(config|data|index|schema)$")) ? data : std::string("config");
    std::string _path = std::string("/var/app/data/") + arg;
    if (FILE *_f = std::fopen(_path.c_str(), "w")) std::fclose(_f);
}
