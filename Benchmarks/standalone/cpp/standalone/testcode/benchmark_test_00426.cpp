// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>

void benchmark_test_00426(int, char **)
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
    static const char *_allowed[] = { "report.pdf", "invoice.csv", "summary.txt" };
    std::string _picked = "report.pdf";
    for (const char *_a : _allowed) if (user_input == _a) { _picked = _a; break; }
    std::string safe = std::string("/var/app/data/") + _picked;
    if (FILE *_f = std::fopen(safe.c_str(), "r")) std::fclose(_f);
}
