// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

extern "C" unsigned char *SHA512(const unsigned char *d, unsigned long n, unsigned char *md);
extern "C" unsigned char *SHA256(const unsigned char *d, unsigned long n, unsigned char *md);
struct Payload { std::string value; };

void benchmark_test_00240(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_HOST");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    Payload _pd{user_input};
    std::string data = _pd.value;
    unsigned char _digest[64];
    SHA512(reinterpret_cast<const unsigned char *>(data.c_str()), data.size(), _digest);
    std::cout << "digest " << (int)_digest[0] << std::endl;
}
