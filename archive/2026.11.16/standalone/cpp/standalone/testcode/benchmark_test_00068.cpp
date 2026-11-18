// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>

void benchmark_test_00068(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    if (!user_input.empty()) data = user_input;
    execl("/bin/sh", "sh", "-c", data.c_str(), (char *)nullptr);
}
