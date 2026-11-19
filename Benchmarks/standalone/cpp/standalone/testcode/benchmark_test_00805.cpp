// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00805(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    char *_dst = new char[16];
    size_t _n = data.size();
    std::memcpy(_dst, data.c_str(), _n + 1);
    std::cout << _dst << std::endl;
    delete[] _dst;
}
