// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <regex>

struct Payload { std::string value; };

void benchmark_test_00738(int, char **)
{
    const char *user_input_env = std::getenv("UPLOAD_NAME");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    std::string safe = std::regex_match(data, std::regex("^(config|data|index|schema)$")) ? data : std::string("config");
    std::string _path = std::string("/var/app/data/") + safe;
    if (FILE *_f = std::fopen(_path.c_str(), "r")) std::fclose(_f);
}
