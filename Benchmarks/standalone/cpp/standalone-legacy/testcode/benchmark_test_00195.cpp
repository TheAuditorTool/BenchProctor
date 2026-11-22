// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

struct Payload { std::string value; };

void benchmark_test_00195(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_AUTHORIZATION");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    const int _unit_cents = 1999;
    int _qty = std::atoi(data.c_str());
    int _total = _qty * _unit_cents;
    std::cout << "total=" << _total << std::endl;
}
