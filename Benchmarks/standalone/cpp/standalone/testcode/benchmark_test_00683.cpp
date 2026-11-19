// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00683(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::cout << _p << std::endl;
    if (std::strchr(_p, ';') != nullptr) { delete[] _p; return; }
    delete[] _p;
}
