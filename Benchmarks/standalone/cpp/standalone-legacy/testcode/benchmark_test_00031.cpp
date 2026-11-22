// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <climits>

void benchmark_test_00031(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data = !user_input.empty() ? user_input : std::string();
    std::string _joined = std::string("/var/app/data/") + data;
    char _resolved[PATH_MAX];
    if (!realpath(_joined.c_str(), _resolved)) return;
    if (std::string(_resolved).rfind("/var/app/data/", 0) != 0) return;
    std::string arg = _resolved;
    std::remove(arg.c_str());
}
