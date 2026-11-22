// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00193(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string arg;
    for (char _c : data) {
        if (_c == '&') arg += "&amp;";
        else if (_c == '<') arg += "&lt;";
        else if (_c == '>') arg += "&gt;";
        else if (_c == '"') arg += "&quot;";
        else if (_c == '\'') arg += "&#39;";
        else arg.push_back(_c);
    }
    std::string _page = "<section class=\"profile\" title=\"{{name}}\"><h2>{{name}}</h2></section>";
    std::string::size_type _at = 0;
    while ((_at = _page.find("{{name}}", _at)) != std::string::npos) {
        _page.replace(_at, 8, arg);
        _at += arg.size();
    }
    std::cout << "Content-Type: text/html\r\n\r\n" << _page << std::endl;
}
