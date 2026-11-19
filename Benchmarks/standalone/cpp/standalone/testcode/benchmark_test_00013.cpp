// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>

void benchmark_test_00013(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    char *_dst = new char[32];
    std::snprintf(_dst, 32, "user=%s", data.c_str());
    std::cout << _dst << std::endl;
    delete[] _dst;
}
