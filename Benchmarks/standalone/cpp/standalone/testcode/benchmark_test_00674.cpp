// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00674(int, char **)
{
    const char *user_input_env = std::getenv("PATH_INFO");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
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
