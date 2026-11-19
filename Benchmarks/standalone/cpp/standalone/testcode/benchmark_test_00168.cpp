// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>
#include <filesystem>

void benchmark_test_00168(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    std::string safe = std::string("/var/app/data/") + std::filesystem::path(data).filename().string();
    if (FILE *_f = std::fopen(safe.c_str(), "w")) std::fclose(_f);
}
