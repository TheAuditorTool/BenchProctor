// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

struct Payload { std::string value; };

void benchmark_test_00239(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    const char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = std::strtoul(data.c_str(), nullptr, 10);
    if (_span > sizeof(_out)) _span = sizeof(_out);
    std::memcpy(_out, _buf, _span);
    std::cout << std::string(_out, _span).size() << std::endl;
}
