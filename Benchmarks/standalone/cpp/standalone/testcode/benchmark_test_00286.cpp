// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <regex>

void benchmark_test_00286(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    static const std::regex _re("^[a-zA-Z0-9 _.#%\\-]+$");
    std::string arg = std::regex_match(user_input, _re) ? user_input : std::string("default");
    std::string _html = std::string("<div class=\"comment\" data-author=\"") + arg + "\">" + arg + "</div>";
    std::fputs("Content-Type: text/html\r\n\r\n", stdout);
    std::fwrite(_html.data(), 1, _html.size(), stdout);
}
