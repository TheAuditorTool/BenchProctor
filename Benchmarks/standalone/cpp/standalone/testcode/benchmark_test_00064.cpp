// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <unistd.h>

void benchmark_test_00064(int, char **)
{
    std::string user_input;
    if (FILE *_fp = std::fopen("/tmp/data", "r")) {
        char _b[256];
        if (std::fgets(_b, sizeof(_b), _fp)) {
            _b[std::strcspn(_b, "\n")] = 0;
            user_input = _b;
        }
        std::fclose(_fp);
    }
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    const char _buf[16] = "fixedcontent12";
    size_t _span = std::strtoul(data.c_str(), nullptr, 10);
    if (_span > sizeof(_buf)) _span = sizeof(_buf);
    std::cout.write(_buf, static_cast<std::streamsize>(_span));
    std::cout << std::endl;
}
