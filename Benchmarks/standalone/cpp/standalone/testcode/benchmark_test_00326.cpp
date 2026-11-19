// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00326(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    const char _buf[16] = "fixedcontent12";
    int _i = std::atoi(data.c_str());
    std::cout << _buf[_i] << std::endl;
}
