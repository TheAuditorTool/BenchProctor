// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>

void benchmark_test_00784(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    int _x = 0;
    if (!data.empty()) _x = (int)data[0];
    std::cout << (_x + (int)data.size()) << std::endl;
}
