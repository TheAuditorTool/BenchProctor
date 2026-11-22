// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

struct Payload { std::string value; };

void benchmark_test_00092(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    size_t _n = data.size();
    char *_p = new char[_n + 1];
    std::memcpy(_p, data.c_str(), _n + 1);
    std::cout << _p << std::endl;
    std::memset(_p, 0, _n + 1);
    delete[] _p;
}
