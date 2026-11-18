// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <climits>

void benchmark_test_00523(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    std::string _joined = std::string("/var/app/data/") + data;
    char _resolved[PATH_MAX];
    if (!realpath(_joined.c_str(), _resolved)) return;
    if (std::string(_resolved).rfind("/var/app/data/", 0) != 0) return;
    std::string safe = _resolved;
    std::remove(safe.c_str());
}
