// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00091(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_USER_AGENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    char *_p = new char[16];
    std::strcpy(_p, "pending");
    std::cout << _p << std::endl;
    _p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::cout << _p << std::endl;
    delete[] _p;
}
