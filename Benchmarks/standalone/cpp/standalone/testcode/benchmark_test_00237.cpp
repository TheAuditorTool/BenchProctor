// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

void benchmark_test_00237(int, char **)
{
    const char *user_input_env = std::getenv("PATH_INFO");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::cout << "Content-Type: text/html\r\n\r\n" << (std::string("<div class=\"comment\" data-author=\"") + user_input + "\">" + user_input + "</div>") << std::endl;
}
