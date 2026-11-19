// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

struct Payload { std::string value; };

void benchmark_test_00666(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    std::srand((unsigned)std::time(nullptr));
    int _token = std::rand();
    std::cout << "token for " << data << ": " << _token << std::endl;
}
