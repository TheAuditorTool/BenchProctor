// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>
#include <regex>

void benchmark_test_00389(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::string safe = std::regex_match(data, std::regex("^(status|info|list|show)$")) ? data : std::string("status");
    execl("/bin/sh", "sh", "-c", safe.c_str(), (char *)nullptr);
}
