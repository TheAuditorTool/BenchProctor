// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

struct Payload { std::string value; };

void benchmark_test_00206(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    delete[] _p;
    _p = nullptr;
}
