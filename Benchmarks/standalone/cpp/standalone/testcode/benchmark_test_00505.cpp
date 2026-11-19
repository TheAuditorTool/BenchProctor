// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00505(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_USER_AGENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    const char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = std::strtoul(data.c_str(), nullptr, 10);
    if (_span > sizeof(_out)) _span = sizeof(_out);
    std::memcpy(_out, _buf, _span);
    std::cout << std::string(_out, _span).size() << std::endl;
}
