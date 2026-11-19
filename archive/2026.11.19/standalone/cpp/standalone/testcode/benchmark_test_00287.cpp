// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00287(int, char **)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string safe = (user_input == "/bin/echo" || user_input == "/bin/cat") ? user_input : std::string("/bin/echo");
    const char *_argv[] = { safe.c_str(), nullptr };
    execv(safe.c_str(), const_cast<char *const *>(_argv));
}
