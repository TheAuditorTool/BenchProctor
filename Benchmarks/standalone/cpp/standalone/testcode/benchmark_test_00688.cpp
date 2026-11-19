// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <filesystem>

void benchmark_test_00688(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_ORIGIN");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    std::string safe = std::string("/var/app/data/") + std::filesystem::path(data).filename().string();
    std::remove(safe.c_str());
}
