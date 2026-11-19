// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <unistd.h>

void benchmark_test_00725(int, char **)
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
    const char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = std::strtoul(user_input.c_str(), nullptr, 10);
    if (_span > sizeof(_buf)) _span = sizeof(_buf);
    std::memcpy(_out, _buf, _span);
    std::cout << std::string(_out, _span).size() << std::endl;
}
