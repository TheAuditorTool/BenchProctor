// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

void benchmark_test_00115(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_USER_AGENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    static const std::regex _re("^[a-zA-Z0-9 _.#%\\-]+$");
    std::string safe = std::regex_match(user_input, _re) ? user_input : std::string("default");
    std::cout << "Content-Type: text/html\r\n\r\n" << (std::string("<div class=\"comment\" data-author=\"") + safe + "\">" + safe + "</div>") << std::endl;
}
