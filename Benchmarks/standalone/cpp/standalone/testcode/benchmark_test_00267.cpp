// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <unistd.h>

void benchmark_test_00267(int, char **)
{
    std::string user_input;
    if (FILE *_fp = std::fopen("/tmp/data", "r")) {
        char _b[256];
        if (std::fgets(_b, sizeof(_b), _fp)) {
            _b[std::strcspn(_b, "\n")] = 0;
            user_input = _b;
        }
        std::fclose(_fp);
    }
    std::string data = !user_input.empty() ? user_input : std::string();
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    if (std::strchr(_p, ';') != nullptr) return;
    std::cout << _p << std::endl;
    delete[] _p;
}
