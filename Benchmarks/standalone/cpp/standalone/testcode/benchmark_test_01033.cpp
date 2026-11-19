// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_01033(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_FORWARDED_FOR");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    const int _unit_cents = 1999;
    int _qty = std::atoi(user_input.c_str());
    int _total = _qty * _unit_cents;
    std::cout << "total=" << _total << std::endl;
}
