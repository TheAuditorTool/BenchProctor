// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00393(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data = cpp_own(user_input);
    std::string arg = (data == "/bin/echo" || data == "/bin/cat") ? data : std::string("/bin/echo");
    const char *_argv[] = { arg.c_str(), nullptr };
    execv(arg.c_str(), const_cast<char *const *>(_argv));
}
