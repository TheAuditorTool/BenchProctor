// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00840(int, char **)
{
    const char *user_input_env = std::getenv("QUERY_STRING");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::cout << "Content-Type: text/html\r\n\r\n" << (std::string("<div class=\"comment\" data-author=\"") + data + "\">" + data + "</div>") << std::endl;
}
