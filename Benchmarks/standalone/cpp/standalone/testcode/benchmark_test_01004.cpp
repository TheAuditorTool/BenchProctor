// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_01004(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    for (std::string::size_type _i = 0; _i < user_input.size(); ++_i) {
        if (user_input[_i] == '%' && _i + 2 < user_input.size()) {
            data.push_back((char)std::strtol(user_input.substr(_i + 1, 2).c_str(), nullptr, 16));
            _i += 2;
        } else { data.push_back(user_input[_i]); }
    }
    const size_t _rec_size = 64;
    long _count = std::strtol(data.c_str(), nullptr, 10);
    if (_count <= 0 || _count > 65536) return;
    size_t _bytes = (size_t)_count * _rec_size;
    char *_recs = new (std::nothrow) char[_bytes];
    delete[] _recs;
}
