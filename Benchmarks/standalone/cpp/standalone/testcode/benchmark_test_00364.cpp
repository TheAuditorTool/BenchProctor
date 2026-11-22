// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <unistd.h>
#include <random>

void benchmark_test_00364(int, char **)
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
    std::mt19937 _gen(static_cast<std::mt19937::result_type>(std::time(nullptr)));
    std::uniform_int_distribution<int> _dist(0, 999999);
    int _token = _dist(_gen);
    std::cout << "token for " << user_input << ": " << _token << std::endl;
}
