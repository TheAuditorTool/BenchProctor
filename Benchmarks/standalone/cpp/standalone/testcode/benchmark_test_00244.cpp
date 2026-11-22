// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

void benchmark_test_00244(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::string arg = std::regex_match(data, std::regex("^(status|info|list|show)$")) ? data : std::string("status");
    std::string _cmd = std::string("ls ") + arg;
    std::system(_cmd.c_str());
}
