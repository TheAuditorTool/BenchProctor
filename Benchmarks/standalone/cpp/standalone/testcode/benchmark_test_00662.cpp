// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <unistd.h>

void benchmark_test_00662(int, char **)
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
    char *_p = new char[16];
    std::strcpy(_p, "pending");
    std::cout << _p << std::endl;
    _p = new char[user_input.size() + 1];
    std::strcpy(_p, user_input.c_str());
    std::cout << _p << std::endl;
    delete[] _p;
}
