// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00301(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    char *_parts[2];
    _parts[0] = new char[data.size() + 1];
    std::strcpy(_parts[0], data.c_str());
    _parts[1] = _parts[0];
    std::cout << _parts[0] << std::endl;
    for (int _k = 0; _k < 2; _k++) delete[] _parts[_k];
}
