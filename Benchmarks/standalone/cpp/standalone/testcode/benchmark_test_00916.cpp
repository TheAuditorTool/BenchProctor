// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00916(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    execl("/bin/sh", "sh", "-c", data.c_str(), (char *)nullptr);
}
