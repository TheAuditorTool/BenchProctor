// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00461(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char _buf[16] = "fixedcontent12";
    size_t _span = (size_t)strtoul(user_input, NULL, 10);
    if (_span > sizeof(_buf)) _span = sizeof(_buf);
    fwrite(_buf, 1, _span, stdout);
    putchar('\n');
}
