// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00504(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = cpp_own(user_input);
    std::string _html = std::string("<div class=\"comment\" data-author=\"") + data + "\">" + data + "</div>";
    std::fputs("Content-Type: text/html\r\n\r\n", stdout);
    std::fwrite(_html.data(), 1, _html.size(), stdout);
}
