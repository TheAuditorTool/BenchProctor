// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00214(int, char **)
{
    const char *user_input_env = std::getenv("API_RESPONSE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    std::string _loc = data;
    for (char &_c : _loc) if (_c == '\r' || _c == '\n') _c = ' ';
    const std::string _refresh = "Refresh: 0; url=" + _loc + "\r\n\r\n";
    std::cout.write(_refresh.data(), static_cast<std::streamsize>(_refresh.size()));
}
