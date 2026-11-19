// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <filesystem>

void benchmark_test_00302(int, char **)
{
    const char *user_input_env = std::getenv("UPLOAD_NAME");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    std::string safe = std::string("/var/app/data/") + std::filesystem::path(data).filename().string();
    std::remove(safe.c_str());
}
