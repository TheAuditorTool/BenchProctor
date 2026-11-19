// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>

void benchmark_test_00626(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    static const char *_allowed[] = { "report.pdf", "invoice.csv", "summary.txt" };
    std::string _picked = "report.pdf";
    for (const char *_a : _allowed) if (data == _a) { _picked = _a; break; }
    std::string safe = std::string("/var/app/data/") + _picked;
    if (FILE *_f = std::fopen(safe.c_str(), "w")) std::fclose(_f);
}
