// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

extern "C" unsigned char *MD5(const unsigned char *d, unsigned long n, unsigned char *md);

void benchmark_test_00606(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_ORIGIN");
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
    unsigned char _digest[16];
    MD5(reinterpret_cast<const unsigned char *>(data.c_str()), data.size(), _digest);
    std::cout << "digest " << (int)_digest[0] << std::endl;
}
