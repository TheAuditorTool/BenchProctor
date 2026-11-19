// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00453(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = cpp_own(user_input);
    const long _unit_cents = 1999;
    long _qty = std::strtol(data.c_str(), nullptr, 10);
    if (_qty < 0 || _qty > 100000) return;
    long _total = _qty * _unit_cents;
    std::cout << "total=" << _total << std::endl;
}
