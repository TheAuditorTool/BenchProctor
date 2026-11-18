// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>
#include <regex>

void benchmark_test_00615(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    static const std::regex _schema("^[a-zA-Z0-9 _.%\\-]+$");
    if (!std::regex_match(data, _schema)) return;
    std::string safe = data;
    std::string _cmd = std::string("grep ") + safe + " /var/log/app.log";
    FILE *_p = popen(_cmd.c_str(), "r");
    if (_p) pclose(_p);
}
