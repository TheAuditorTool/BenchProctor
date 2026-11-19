// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <unistd.h>

void benchmark_test_00176(int, char **)
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
    std::srand((unsigned)std::time(nullptr));
    int _token = std::rand();
    std::cout << "token for " << data << ": " << _token << std::endl;
}
