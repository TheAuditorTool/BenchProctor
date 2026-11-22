// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

void benchmark_test_00023(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    std::string arg;
    for (char _c : data) {
        if (_c == '&') arg += "&amp;";
        else if (_c == '<') arg += "&lt;";
        else if (_c == '>') arg += "&gt;";
        else if (_c == '"') arg += "&quot;";
        else if (_c == '\'') arg += "&#39;";
        else arg.push_back(_c);
    }
    std::cout << "Content-Type: text/html\r\n\r\n" << (std::string("<div class=\"comment\" data-author=\"") + arg + "\">" + arg + "</div>") << std::endl;
}
