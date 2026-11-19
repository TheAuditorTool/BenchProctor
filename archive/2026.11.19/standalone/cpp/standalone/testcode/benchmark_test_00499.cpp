// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

struct Payload { std::string value; };

void benchmark_test_00499(int argc, char **argv)
{
    std::string user_input = (argc > 2) ? std::string(argv[2]) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::string _out(_p);
    delete[] _p;
    std::cout << _out << std::endl;
}
