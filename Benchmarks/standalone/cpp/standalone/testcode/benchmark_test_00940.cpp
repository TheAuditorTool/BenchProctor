// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00940(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _doc = std::string("{\"field\":\"") + user_input + "\"}";
    std::string::size_type _fs = _doc.find("\"field\":\"") + 9;
    std::string::size_type _fe = _doc.find('"', _fs);
    std::string data = _doc.substr(_fs, _fe - _fs);
    char *_p = new char[16];
    std::strcpy(_p, "pending");
    std::cout << _p << std::endl;
    _p = new char[data.size() + 1];
    std::strcpy(_p, data.c_str());
    std::cout << _p << std::endl;
    delete[] _p;
}
