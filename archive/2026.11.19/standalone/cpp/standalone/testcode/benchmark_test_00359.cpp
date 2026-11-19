// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <unistd.h>

struct Payload { std::string value; };

void benchmark_test_00359(int, char **)
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
    Payload _pd{user_input};
    std::string data = _pd.value;
    char _dst[16];
    std::strcpy(_dst, data.c_str());
    std::cout << _dst << std::endl;
}
