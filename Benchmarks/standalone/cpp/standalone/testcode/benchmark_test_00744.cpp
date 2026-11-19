// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>
#include <regex>

void benchmark_test_00744(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    static const std::regex _schema("^[a-zA-Z0-9 _.%\\-]+$");
    if (!std::regex_match(user_input, _schema)) return;
    std::string safe = user_input;
    std::string _cmd = std::string("grep ") + safe + " /var/log/app.log";
    FILE *_p = popen(_cmd.c_str(), "r");
    if (_p) pclose(_p);
}
