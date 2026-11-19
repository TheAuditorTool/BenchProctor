// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>

void benchmark_test_00704(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    int _x;
    if (!data.empty()) _x = (int)data[0];
    std::cout << (_x + (int)data.size()) << std::endl;
}
