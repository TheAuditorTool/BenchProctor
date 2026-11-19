// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <regex>

void benchmark_test_00865(int, char **)
{
    std::string user_input;
    if (const char *user_input_cl = std::getenv("CONTENT_LENGTH")) {
        long user_input_n = std::strtol(user_input_cl, nullptr, 10);
        if (user_input_n > 0 && user_input_n < 1048576) {
            user_input.resize((size_t)user_input_n);
            std::cin.read(&user_input[0], user_input_n);
            user_input.resize((size_t)std::cin.gcount());
        }
    }
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    static const std::regex _re("^[a-zA-Z0-9 _.#~\\-]+$");
    std::string safe = std::regex_match(data, _re) ? data : std::string("default");
    std::string _path = std::string("/var/app/data/") + safe;
    std::remove(_path.c_str());
}
