// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <filesystem>

struct Payload { std::string value; };

void benchmark_test_00035(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    Payload _pd{user_input};
    std::string data = _pd.value;
    std::string safe = std::string("/var/app/data/") + std::filesystem::path(data).filename().string();
    std::remove(safe.c_str());
}
