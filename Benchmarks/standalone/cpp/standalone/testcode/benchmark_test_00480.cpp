// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00480(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    const char _buf[16] = "fixedcontent12";
    size_t _span = std::strtoul(data.c_str(), nullptr, 10);
    std::cout.write(_buf, static_cast<std::streamsize>(_span));
    std::cout << std::endl;
}
