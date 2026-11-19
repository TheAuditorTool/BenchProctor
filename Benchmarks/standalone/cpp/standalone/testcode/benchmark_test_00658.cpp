// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

void benchmark_test_00658(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    const char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = std::strtoul(data.c_str(), nullptr, 10);
    if (_span > sizeof(_buf)) _span = sizeof(_buf);
    std::memcpy(_out, _buf, _span);
    std::cout << std::string(_out, _span).size() << std::endl;
}
