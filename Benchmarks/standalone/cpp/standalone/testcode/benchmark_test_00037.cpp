// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00037(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    std::string _loc = data;
    for (char &_c : _loc) if (_c == '\r' || _c == '\n') _c = ' ';
    std::fprintf(stdout, "Status: 302 Found\r\nLocation: %s\r\n\r\n", _loc.c_str());
}
