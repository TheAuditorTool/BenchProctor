// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <regex>

void benchmark_test_00347(int, char **)
{
    const char *user_input_env = std::getenv("UPLOAD_NAME");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    static const std::regex _re("^[a-zA-Z0-9 _.#~\\-]+$");
    std::string safe = std::regex_match(data, _re) ? data : std::string("default");
    std::string _path = std::string("/var/app/data/") + safe;
    if (FILE *_f = std::fopen(_path.c_str(), "r")) std::fclose(_f);
}
