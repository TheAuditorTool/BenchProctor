// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00585(int, char **)
{
    const char *user_input_env = std::getenv("UPLOAD_FILENAME");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    int _req = std::atoi(data.c_str());
    int _alloc = _req + 1;
    char *_buf = new (std::nothrow) char[(size_t)_alloc];
    if (_buf) { _buf[0] = 0; std::cout << "alloc:" << _alloc << std::endl; delete[] _buf; }
}
