// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00180(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    std::string _ckval = data;
    std::printf("Set-Cookie: session=%s; HttpOnly; SameSite=Strict; Path=/\r\n", _ckval.c_str());
}
