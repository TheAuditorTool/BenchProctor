// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <fcntl.h>

void benchmark_test_00058(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_COOKIE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    unsigned char _rnd[16];
    int _fd = open("/dev/urandom", O_RDONLY);
    if (_fd >= 0) { if (read(_fd, _rnd, sizeof(_rnd)) < 0) _rnd[0] = 0; close(_fd); }
    std::cout << "token for " << data << ": " << (int)_rnd[0] << std::endl;
}
