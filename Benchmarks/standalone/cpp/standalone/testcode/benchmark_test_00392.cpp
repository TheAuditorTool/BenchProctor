// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>

void benchmark_test_00392(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    int _x;
    if (!user_input.empty()) _x = (int)user_input[0];
    std::cout << (_x + (int)user_input.size()) << std::endl;
}
