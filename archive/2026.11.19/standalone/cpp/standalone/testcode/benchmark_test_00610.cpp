// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

struct Payload { std::string value; };

void benchmark_test_00610(int, char **)
{
    const char *user_input_env = std::getenv("USER_COMMENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    int _req = std::atoi(data.c_str());
    int _alloc = _req + 1;
    char *_buf = new (std::nothrow) char[(size_t)_alloc];
    if (_buf) { _buf[0] = 0; std::cout << "alloc:" << _alloc << std::endl; delete[] _buf; }
}
