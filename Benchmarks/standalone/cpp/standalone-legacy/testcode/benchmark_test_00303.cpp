// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00303(int, char **)
{
    const char *user_input_env = std::getenv("API_RESPONSE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    std::string _loc = data;
    for (char &_c : _loc) if (_c == '\r' || _c == '\n') _c = ' ';
    const std::string _refresh = "Refresh: 0; url=" + _loc + "\r\n\r\n";
    std::cout.write(_refresh.data(), static_cast<std::streamsize>(_refresh.size()));
}
