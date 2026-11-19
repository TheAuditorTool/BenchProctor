// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>

void benchmark_test_00339(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    char *_dst = new char[32];
    std::snprintf(_dst, 32, "user=%s", data.c_str());
    std::cout << _dst << std::endl;
    delete[] _dst;
}
