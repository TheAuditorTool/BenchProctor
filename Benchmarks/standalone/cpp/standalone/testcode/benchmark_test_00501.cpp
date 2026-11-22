// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>

struct Payload { std::string value; };

void benchmark_test_00501(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    Payload _pd{user_input};
    std::string data = _pd.value;
    size_t _n = data.size();
    int _mode;
    if (_n > 64) _mode = 2;
    else if (_n > 0) _mode = 1;
    std::cout << _mode << std::endl;
}
