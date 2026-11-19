// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00152(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    char *_dst = new char[32];
    std::sprintf(_dst, "user=%s", data.c_str());
    std::cout << _dst << std::endl;
    delete[] _dst;
}
