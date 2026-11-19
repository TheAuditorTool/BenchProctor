// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>
#include <regex>

void benchmark_test_00887(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    static const std::regex _schema("^[a-zA-Z0-9 _.%\\-]+$");
    if (!std::regex_match(data, _schema)) return;
    std::string safe = data;
    execl("/bin/sh", "sh", "-c", safe.c_str(), (char *)nullptr);
}
