// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00629(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    for (std::string::size_type _i = 0; _i < user_input.size(); ++_i) {
        if (user_input[_i] == '%' && _i + 2 < user_input.size()) {
            data.push_back((char)std::strtol(user_input.substr(_i + 1, 2).c_str(), nullptr, 16));
            _i += 2;
        } else { data.push_back(user_input[_i]); }
    }
    std::string safe = (data == "/bin/echo" || data == "/bin/cat") ? data : std::string("/bin/echo");
    const char *_argv[] = { safe.c_str(), nullptr };
    execv(safe.c_str(), const_cast<char *const *>(_argv));
}
