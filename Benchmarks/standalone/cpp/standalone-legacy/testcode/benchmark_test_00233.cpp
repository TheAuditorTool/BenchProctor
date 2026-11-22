// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

struct Payload { std::string value; };

void benchmark_test_00233(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    Payload _pd{user_input};
    std::string data = _pd.value;
    const char _buf[16] = "fixedcontent12";
    int _i = std::atoi(data.c_str());
    std::cout << _buf[_i] << std::endl;
}
