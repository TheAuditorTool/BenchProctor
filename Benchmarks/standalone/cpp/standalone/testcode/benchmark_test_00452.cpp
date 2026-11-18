// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

extern "C" unsigned char *SHA256(const unsigned char *d, unsigned long n, unsigned char *md);

void benchmark_test_00452(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    unsigned char _digest[32];
    SHA256(reinterpret_cast<const unsigned char *>(user_input.c_str()), user_input.size(), _digest);
    std::cout << "digest " << (int)_digest[0] << std::endl;
}
