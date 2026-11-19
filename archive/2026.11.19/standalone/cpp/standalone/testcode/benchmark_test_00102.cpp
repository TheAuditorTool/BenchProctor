// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00102(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char *_p = new char[user_input.size() + 1];
    std::strcpy(_p, user_input.c_str());
    std::string _out(_p);
    delete[] _p;
    std::cout << _out << std::endl;
}
