// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00459(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    if (!user_input.empty()) data = user_input;
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    if (std::strchr(_p, ';') != nullptr) return;
    std::cout << _p << std::endl;
    delete[] _p;
}
