// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <unistd.h>

void benchmark_test_00735(int, char **)
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
    std::string _doc = std::string("{\"field\":\"") + user_input + "\"}";
    std::string::size_type _fs = _doc.find("\"field\":\"") + 9;
    std::string::size_type _fe = _doc.find('"', _fs);
    std::string data = _doc.substr(_fs, _fe - _fs);
    char _dst[16];
    std::strcpy(_dst, data.c_str());
    std::cout << _dst << std::endl;
}
