// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00412(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    const char *_argv[] = { "/usr/bin/grep", user_input.c_str(), nullptr };
    execv("/usr/bin/grep", const_cast<char *const *>(_argv));
}
