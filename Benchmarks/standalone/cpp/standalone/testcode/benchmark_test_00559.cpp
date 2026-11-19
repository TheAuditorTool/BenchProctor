// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00559(int, char **)
{
    const char *user_input_env = std::getenv("MULTIPART_FIELD");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    std::cout << "Location: " << data << std::endl;
}
