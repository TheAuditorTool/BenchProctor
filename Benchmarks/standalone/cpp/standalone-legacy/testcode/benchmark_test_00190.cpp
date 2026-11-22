// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00190(int, char **)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string arg = (data == "/bin/echo" || data == "/bin/cat") ? data : std::string("/bin/echo");
    const char *_argv[] = { arg.c_str(), nullptr };
    execv(arg.c_str(), const_cast<char *const *>(_argv));
}
