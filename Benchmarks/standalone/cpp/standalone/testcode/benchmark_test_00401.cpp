// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>

void benchmark_test_00401(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    std::string _path = std::string("/var/app/data/") + data;
    if (FILE *_f = std::fopen(_path.c_str(), "r")) std::fclose(_f);
}
