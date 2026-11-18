// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00355(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    std::string safe;
    for (char _c : data) {
        if (_c == '&') safe += "&amp;";
        else if (_c == '<') safe += "&lt;";
        else if (_c == '>') safe += "&gt;";
        else if (_c == '"') safe += "&quot;";
        else if (_c == '\'') safe += "&#39;";
        else safe.push_back(_c);
    }
    std::cout << "Content-Type: text/html\r\n\r\n" << (std::string("<div class=\"comment\" data-author=\"") + safe + "\">" + safe + "</div>") << std::endl;
}
