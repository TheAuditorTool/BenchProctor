// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>

struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00103(int, char **)
{
    const char *user_input_env = std::getenv("USER_COMMENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    static const char *_allowed[] = { "report.pdf", "invoice.csv", "summary.txt" };
    std::string _picked = "report.pdf";
    for (const char *_a : _allowed) if (data == _a) { _picked = _a; break; }
    std::string safe = std::string("/var/app/data/") + _picked;
    if (FILE *_f = std::fopen(safe.c_str(), "w")) std::fclose(_f);
}
