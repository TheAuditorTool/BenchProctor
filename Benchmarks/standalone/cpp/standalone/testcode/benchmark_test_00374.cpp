// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <unistd.h>

void benchmark_test_00374(int, char **)
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
    struct { int id; int flags; } _rec;
    _rec.id = std::atoi(user_input.c_str());
    std::cout << _rec.id << " " << _rec.flags << std::endl;
}
