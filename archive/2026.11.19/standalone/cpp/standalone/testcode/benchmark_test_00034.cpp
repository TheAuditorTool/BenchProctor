// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

struct Payload { std::string value; };

void benchmark_test_00034(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_USER_AGENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    char *_dst = new char[16];
    std::strncpy(_dst, data.c_str(), 15);
    _dst[15] = '\0';
    delete[] _dst;
}
