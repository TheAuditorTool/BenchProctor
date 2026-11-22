// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00349(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    const size_t _rec_size = 64;
    long _count = std::strtol(data.c_str(), nullptr, 10);
    if (_count <= 0 || _count > 65536) return;
    size_t _bytes = (size_t)_count * _rec_size;
    char *_recs = new (std::nothrow) char[_bytes];
    delete[] _recs;
}
