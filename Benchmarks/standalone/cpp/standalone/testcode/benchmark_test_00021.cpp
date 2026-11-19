// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00021(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    const char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = std::strtoul(data.c_str(), nullptr, 10);
    if (_span > sizeof(_buf)) _span = sizeof(_buf);
    std::memcpy(_out, _buf, _span);
    std::cout << std::string(_out, _span).size() << std::endl;
}
