// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <fcntl.h>

void benchmark_test_00900(int, char **)
{
    const char *user_input_env = std::getenv("PATH_INFO");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    unsigned char _rnd[16];
    int _fd = open("/dev/urandom", O_RDONLY);
    if (_fd >= 0) { if (read(_fd, _rnd, sizeof(_rnd)) < 0) _rnd[0] = 0; close(_fd); }
    std::cout << "token for " << data << ": " << (int)_rnd[0] << std::endl;
}
