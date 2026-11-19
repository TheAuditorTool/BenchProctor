// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

void benchmark_test_00297(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    char *_parts[2];
    _parts[0] = new char[user_input.size() + 1];
    std::strcpy(_parts[0], user_input.c_str());
    _parts[1] = _parts[0];
    std::cout << _parts[0] << std::endl;
    for (int _k = 0; _k < 2; _k++) delete[] _parts[_k];
}
