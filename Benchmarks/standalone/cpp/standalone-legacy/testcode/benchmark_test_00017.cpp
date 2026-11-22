// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00017(int, char **)
{
    const char *user_input_env = std::getenv("MULTIPART_FIELD");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    std::string _loc = data;
    for (char &_c : _loc) if (_c == '\r' || _c == '\n') _c = ' ';
    std::fprintf(stdout, "Status: 302 Found\r\nLocation: %s\r\n\r\n", _loc.c_str());
}
