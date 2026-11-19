// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00552(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data = !user_input.empty() ? user_input : std::string();
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::string _out(_p);
    delete[] _p;
    std::cout << _out << std::endl;
}
