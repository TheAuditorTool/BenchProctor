// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <filesystem>

void benchmark_test_00635(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string safe = std::string("/var/app/data/") + std::filesystem::path(data).filename().string();
    std::remove(safe.c_str());
}
