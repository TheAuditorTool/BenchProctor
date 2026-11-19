// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00561(int, char **)
{
    std::string user_input;
    if (const char *user_input_cl = std::getenv("CONTENT_LENGTH")) {
        long user_input_n = std::strtol(user_input_cl, nullptr, 10);
        if (user_input_n > 0 && user_input_n < 1048576) {
            user_input.resize((size_t)user_input_n);
            std::cin.read(&user_input[0], user_input_n);
            user_input.resize((size_t)std::cin.gcount());
        }
    }
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    long _req = std::strtol(data.c_str(), nullptr, 10);
    if (_req < 0 || _req > 65535) return;
    long _alloc = _req + 1;
    char *_buf = new (std::nothrow) char[(size_t)_alloc];
    if (_buf) { _buf[0] = 0; std::cout << "alloc:" << _alloc << std::endl; delete[] _buf; }
}
