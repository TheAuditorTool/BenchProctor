// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

extern "C" unsigned char *SHA256(const unsigned char *d, unsigned long n, unsigned char *md);

void benchmark_test_00423(int, char **)
{
    const char *user_input_env = std::getenv("USER_COMMENT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    unsigned char _digest[32];
    SHA256(reinterpret_cast<const unsigned char *>(data.c_str()), data.size(), _digest);
    std::cout << "digest " << (int)_digest[0] << std::endl;
}
