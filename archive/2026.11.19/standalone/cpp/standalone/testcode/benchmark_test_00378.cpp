// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00378(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    std::string _cmd = std::string("ls ") + data;
    std::system(_cmd.c_str());
}
