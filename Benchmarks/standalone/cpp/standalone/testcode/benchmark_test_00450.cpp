// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <unistd.h>

struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00450(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    std::string _path = std::string("/var/app/data/") + data;
    if (FILE *_f = std::fopen(_path.c_str(), "r")) std::fclose(_f);
}
