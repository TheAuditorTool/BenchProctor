// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <regex>

void benchmark_test_00582(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    std::string _authority = data;
    std::string::size_type _scheme = _authority.find("://");
    if (_scheme != std::string::npos) _authority = _authority.substr(_scheme + 3);
    else if (_authority.rfind("//", 0) == 0) _authority = _authority.substr(2);
    _authority = _authority.substr(0, _authority.find_first_of("/?#"));
    std::string::size_type _userinfo = _authority.rfind('@');
    if (_userinfo != std::string::npos) _authority = _authority.substr(_userinfo + 1);
    _authority = _authority.substr(0, _authority.find(':'));
    static const std::regex _hw("^(api\\.internal\\.example\\.com|cdn\\.internal\\.example\\.com)$");
    if (!_authority.empty() && !std::regex_match(_authority, _hw)) return;
    std::string safe = data;
    std::cout << "Location: " << safe << std::endl;
}
