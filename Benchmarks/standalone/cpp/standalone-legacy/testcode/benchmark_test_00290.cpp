// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00290(int, char **)
{
    const char *user_input_env = std::getenv("UPLOAD_FILENAME");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    const int _unit_cents = 1999;
    int _qty = std::atoi(data.c_str());
    int _total = _qty * _unit_cents;
    std::cout << "total=" << _total << std::endl;
}
