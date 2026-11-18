// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>

void benchmark_test_00015(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string _cmd = std::string("grep ") + user_input + " /var/log/app.log";
    FILE *_p = popen(_cmd.c_str(), "r");
    if (_p) pclose(_p);
}
