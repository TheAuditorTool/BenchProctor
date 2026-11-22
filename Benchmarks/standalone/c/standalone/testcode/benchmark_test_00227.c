// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00227(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char _dst[16];
    size_t _n = strlen(user_input);
    if (_n >= sizeof(_dst)) _n = sizeof(_dst) - 1;
    memcpy(_dst, user_input, _n);
    _dst[_n] = '\0';
    printf("%s\n", _dst);
}
