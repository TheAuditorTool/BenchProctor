// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

extern "C" int RAND_bytes(unsigned char *buf, int num);

void benchmark_test_00054(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    for (std::string::size_type _i = 0; _i < user_input.size(); ++_i) {
        if (user_input[_i] == '%' && _i + 2 < user_input.size()) {
            data.push_back((char)std::strtol(user_input.substr(_i + 1, 2).c_str(), nullptr, 16));
            _i += 2;
        } else { data.push_back(user_input[_i]); }
    }
    unsigned char _rnd[16];
    if (RAND_bytes(_rnd, sizeof(_rnd)) != 1) return;
    char _hex[33];
    for (int _i = 0; _i < 16; ++_i) std::snprintf(_hex + 2 * _i, 3, "%02x", _rnd[_i]);
    std::cout << "token for " << data << ": " << _hex << std::endl;
}
