// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00023(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::string _html = std::string("<div class=\"comment\" data-author=\"") + data + "\">" + data + "</div>";
    std::fputs("Content-Type: text/html\r\n\r\n", stdout);
    std::fwrite(_html.data(), 1, _html.size(), stdout);
}
