// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>

void benchmark_test_00467(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    size_t _n = data.size();
    int _mode;
    if (_n > 64) _mode = 2;
    else if (_n > 0) _mode = 1;
    else _mode = 0;
    std::cout << _mode << std::endl;
}
