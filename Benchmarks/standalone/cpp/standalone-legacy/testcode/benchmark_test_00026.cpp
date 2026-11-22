// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00026(int, char **)
{
    std::string user_input;
    if (const char *user_input_cl = std::getenv("CONTENT_LENGTH")) {
        long user_input_n = std::strtol(user_input_cl, nullptr, 10);
        if (user_input_n > 0 && user_input_n < 1048576) {
            user_input.resize((size_t)user_input_n);
            std::cin.read(&user_input[0], user_input_n);
            user_input.resize((size_t)std::cin.gcount());
        }
    }
    std::string _doc = std::string("{\"field\":\"") + user_input + "\"}";
    std::string::size_type _fs = _doc.find("\"field\":\"") + 9;
    std::string::size_type _fe = _doc.find('"', _fs);
    std::string data = _doc.substr(_fs, _fe - _fs);
    std::string _page = "<section class=\"profile\" title=\"{{name}}\"><h2>{{name}}</h2></section>";
    std::string::size_type _at = 0;
    while ((_at = _page.find("{{name}}", _at)) != std::string::npos) {
        _page.replace(_at, 8, data);
        _at += data.size();
    }
    std::cout << "Content-Type: text/html\r\n\r\n" << _page << std::endl;
}
