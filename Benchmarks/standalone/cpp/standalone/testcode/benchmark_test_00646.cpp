// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <unistd.h>

void benchmark_test_00646(int, char **)
{
    std::string user_input;
    if (FILE *_fp = std::fopen("/etc/app/config", "r")) {
        char _b[256];
        if (std::fgets(_b, sizeof(_b), _fp)) {
            _b[std::strcspn(_b, "\n")] = 0;
            user_input = _b;
        }
        std::fclose(_fp);
    }
    std::string data;
    if (!user_input.empty()) data = user_input;
    char *_dst = new char[16];
    size_t _n = data.size();
    if (_n > 15) _n = 15;
    std::memcpy(_dst, data.c_str(), _n);
    _dst[_n] = '\0';
    std::cout << _dst << std::endl;
    delete[] _dst;
}
