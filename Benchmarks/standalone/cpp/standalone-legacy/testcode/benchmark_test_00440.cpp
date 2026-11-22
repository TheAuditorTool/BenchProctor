// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

extern "C" int RAND_bytes(unsigned char *buf, int num);

void benchmark_test_00440(int, char **)
{
    const char *user_input_env = std::getenv("UPLOAD_FILENAME");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    unsigned char _rnd[16];
    if (RAND_bytes(_rnd, sizeof(_rnd)) != 1) return;
    char _hex[33];
    for (int _i = 0; _i < 16; ++_i) std::snprintf(_hex + 2 * _i, 3, "%02x", _rnd[_i]);
    std::cout << "token for " << data << ": " << _hex << std::endl;
}
