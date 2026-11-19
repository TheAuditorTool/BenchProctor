// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include <regex>

void benchmark_test_00557(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    std::string safe = std::regex_match(data, std::regex("^(status|info|list|show)$")) ? data : std::string("status");
    std::string _cmd = std::string("grep ") + safe + " /var/log/app.log";
    FILE *_p = popen(_cmd.c_str(), "r");
    if (_p) pclose(_p);
}
