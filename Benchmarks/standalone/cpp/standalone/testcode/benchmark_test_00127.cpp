// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>

void benchmark_test_00127(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    execl("/bin/sh", "sh", "-c", data.c_str(), (char *)nullptr);
}
