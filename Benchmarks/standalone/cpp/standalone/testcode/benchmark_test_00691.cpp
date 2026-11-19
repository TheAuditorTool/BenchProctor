// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00691(int, char **)
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
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    std::string _ckval = data;
    std::printf("Set-Cookie: session=%s; Secure; HttpOnly; SameSite=Strict; Path=/\r\n", _ckval.c_str());
}
