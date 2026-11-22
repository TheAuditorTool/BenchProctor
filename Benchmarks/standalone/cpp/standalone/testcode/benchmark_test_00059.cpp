// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00059(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_FORWARDED_FOR");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = !user_input.empty() ? user_input : std::string();
    std::string _page = "<section class=\"profile\" title=\"{{name}}\"><h2>{{name}}</h2></section>";
    std::string::size_type _at = 0;
    while ((_at = _page.find("{{name}}", _at)) != std::string::npos) {
        _page.replace(_at, 8, data);
        _at += data.size();
    }
    std::cout << "Content-Type: text/html\r\n\r\n" << _page << std::endl;
}
