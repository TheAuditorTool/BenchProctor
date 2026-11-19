// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>

void benchmark_test_00718(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    int _x;
    if (!data.empty()) _x = (int)data[0];
    std::cout << (_x + (int)data.size()) << std::endl;
}
