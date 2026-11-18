// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <fcntl.h>

struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00686(int, char **)
{
    const char *user_input_env = std::getenv("MULTIPART_FIELD");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    unsigned char _rnd[16];
    int _fd = open("/dev/urandom", O_RDONLY);
    if (_fd >= 0) { if (read(_fd, _rnd, sizeof(_rnd)) < 0) _rnd[0] = 0; close(_fd); }
    std::cout << "token for " << data << ": " << (int)_rnd[0] << std::endl;
}
