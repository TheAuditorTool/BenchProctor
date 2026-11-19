// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

extern "C" unsigned char *SHA256(const unsigned char *d, unsigned long n, unsigned char *md);

void benchmark_test_00094(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    unsigned char _digest[32];
    SHA256(reinterpret_cast<const unsigned char *>(data.c_str()), data.size(), _digest);
    std::cout << "digest " << (int)_digest[0] << std::endl;
}
