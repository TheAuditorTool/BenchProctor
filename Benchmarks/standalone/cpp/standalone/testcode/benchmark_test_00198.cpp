// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00198(int, char **)
{
    const char *user_input_env = std::getenv("UPLOAD_FILENAME");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    static const char *_allowed[] = { "report.pdf", "invoice.csv", "summary.txt" };
    std::string _picked = "report.pdf";
    for (const char *_a : _allowed) if (data == _a) { _picked = _a; break; }
    std::string safe = std::string("/var/app/data/") + _picked;
    if (FILE *_f = std::fopen(safe.c_str(), "r")) std::fclose(_f);
}
