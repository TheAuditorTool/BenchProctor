// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00109(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_AUTHORIZATION");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    const int _rec_size = 64;
    int _count = std::atoi(data.c_str());
    int _bytes = _count * _rec_size;
    char *_recs = new (std::nothrow) char[(size_t)_bytes];
    delete[] _recs;
}
