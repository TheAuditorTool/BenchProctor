// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>

void benchmark_test_00439(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    size_t _n = data.size();
    int _mode;
    if (_n > 64) _mode = 2;
    else if (_n > 0) _mode = 1;
    std::cout << _mode << std::endl;
}
