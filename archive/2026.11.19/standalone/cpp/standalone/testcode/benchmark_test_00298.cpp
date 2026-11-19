// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00298(int, char **)
{
    std::string user_input;
    std::getline(std::cin, user_input);
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    const char _buf[16] = "fixedcontent12";
    int _i = std::atoi(data.c_str());
    if (_i >= 0 && _i < (int)sizeof(_buf)) std::cout << _buf[_i] << std::endl;
}
