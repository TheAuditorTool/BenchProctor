// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

struct Payload { std::string value; };

void benchmark_test_00658(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::string _out(_p);
    delete[] _p;
    std::cout << _out << std::endl;
}
