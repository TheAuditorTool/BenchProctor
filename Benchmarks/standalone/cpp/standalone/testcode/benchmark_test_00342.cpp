// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00342(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    char *_p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::string _out(_p);
    delete[] _p;
    std::cout << _out << std::endl;
}
