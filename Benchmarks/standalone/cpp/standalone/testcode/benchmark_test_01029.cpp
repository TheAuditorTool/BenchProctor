// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

void benchmark_test_01029(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    static const std::regex _schema("^[a-zA-Z0-9 _.%\\-]+$");
    if (!std::regex_match(data, _schema)) return;
    std::string safe = data;
    std::string _cmd = std::string("ls ") + safe;
    std::system(_cmd.c_str());
}
