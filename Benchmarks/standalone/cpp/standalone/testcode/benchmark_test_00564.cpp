// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

void benchmark_test_00564(int, char **)
{
    const char *user_input_env = std::getenv("PATH_INFO");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string safe = std::regex_match(user_input, std::regex("^(status|info|list|show)$")) ? user_input : std::string("status");
    std::string _cmd = std::string("ls ") + safe;
    std::system(_cmd.c_str());
}
