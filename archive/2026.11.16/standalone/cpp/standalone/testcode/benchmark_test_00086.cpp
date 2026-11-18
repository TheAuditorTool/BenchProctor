// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>

void benchmark_test_00086(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    const char *_argv[] = { "/usr/bin/grep", data.c_str(), nullptr };
    execv("/usr/bin/grep", const_cast<char *const *>(_argv));
}
