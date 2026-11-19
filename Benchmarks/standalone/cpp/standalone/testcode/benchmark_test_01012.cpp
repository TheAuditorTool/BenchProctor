// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <unistd.h>

void benchmark_test_01012(int, char **)
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
    std::string data;
    if (!user_input.empty()) data = user_input;
    char *_parts[2];
    _parts[0] = new char[data.size() + 1];
    std::strcpy(_parts[0], data.c_str());
    _parts[1] = nullptr;
    std::cout << _parts[0] << std::endl;
    for (int _k = 0; _k < 2; _k++) delete[] _parts[_k];
}
