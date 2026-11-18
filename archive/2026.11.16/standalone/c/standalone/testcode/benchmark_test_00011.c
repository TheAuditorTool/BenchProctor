// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00011(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    const char *data = c_passthrough(user_input);
    char _buf[16] = "fixedcontent12";
    size_t _len = (size_t)strtoul(data, NULL, 10);
    if (_len > sizeof(_buf)) _len = sizeof(_buf);
    unsigned int _sum = 0;
    for (size_t _k = 0; _k < _len; _k++) _sum += (unsigned char)_buf[_k];
    printf("%u\n", _sum);
}
