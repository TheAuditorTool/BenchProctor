// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

struct Payload { std::string value; };

void benchmark_test_00103(int, char **)
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
    Payload _pd{user_input};
    std::string data = _pd.value;
    const char _buf[16] = "fixedcontent12";
    int _i = std::atoi(data.c_str());
    if (_i >= 0 && _i < (int)sizeof(_buf)) std::cout << _buf[_i] << std::endl;
}
