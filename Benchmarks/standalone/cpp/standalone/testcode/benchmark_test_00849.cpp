// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>

void benchmark_test_00849(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    char _dst[16];
    size_t _n = data.size();
    if (_n >= sizeof(_dst)) _n = sizeof(_dst) - 1;
    std::memcpy(_dst, data.c_str(), _n);
    _dst[_n] = '\0';
    std::cout << _dst << std::endl;
}
