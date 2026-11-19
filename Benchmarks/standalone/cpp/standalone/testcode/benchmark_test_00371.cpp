// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

extern "C" unsigned char *MD5(const unsigned char *d, unsigned long n, unsigned char *md);

void benchmark_test_00371(int, char **)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    try { data = user_input; } catch (...) { data.clear(); }
    unsigned char _digest[16];
    MD5(reinterpret_cast<const unsigned char *>(data.c_str()), data.size(), _digest);
    std::cout << "digest " << (int)_digest[0] << std::endl;
}
