// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

void benchmark_test_00059(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string safe = std::regex_match(data, std::regex("^(status|info|list|show)$")) ? data : std::string("status");
    std::string _cmd = std::string("ls ") + safe;
    std::system(_cmd.c_str());
}
