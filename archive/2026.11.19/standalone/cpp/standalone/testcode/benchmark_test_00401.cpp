// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00401(int, char **)
{
    const char *user_input_env = std::getenv("GRAPHQL_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    int _req = std::atoi(data.c_str());
    int _alloc = _req + 1;
    char *_buf = new (std::nothrow) char[(size_t)_alloc];
    if (_buf) { _buf[0] = 0; std::cout << "alloc:" << _alloc << std::endl; delete[] _buf; }
}
