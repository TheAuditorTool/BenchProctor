// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00194(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = cpp_own(user_input);
    std::string safe = (data == "/bin/echo" || data == "/bin/cat") ? data : std::string("/bin/echo");
    const char *_argv[] = { safe.c_str(), nullptr };
    execv(safe.c_str(), const_cast<char *const *>(_argv));
}
