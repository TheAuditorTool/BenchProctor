// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00277(int, char **)
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
