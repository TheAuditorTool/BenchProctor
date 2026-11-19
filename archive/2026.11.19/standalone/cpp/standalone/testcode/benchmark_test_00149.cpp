// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstring>

struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00149(int argc, char **argv)
{
    std::string user_input = (argc > 1) ? std::string(argv[1]) : std::string();
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    char *_dst = new char[16];
    std::strcpy(_dst, data.c_str());
    delete[] _dst;
}
