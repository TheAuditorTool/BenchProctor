// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00427(int, char **)
{
    const char *user_input_env = std::getenv("PATH_INFO");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = cpp_own(user_input);
    static const std::regex _re("^[a-zA-Z0-9 _.#%\\-]+$");
    std::string safe = std::regex_match(data, _re) ? data : std::string("default");
    std::cout << "Content-Type: text/html\r\n\r\n" << (std::string("<div class=\"comment\" data-author=\"") + safe + "\">" + safe + "</div>") << std::endl;
}
