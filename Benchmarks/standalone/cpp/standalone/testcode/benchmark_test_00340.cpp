// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00340(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::cout << _p << std::endl;
    if (std::strchr(_p, ';') != nullptr) delete[] _p;
    delete[] _p;
}
