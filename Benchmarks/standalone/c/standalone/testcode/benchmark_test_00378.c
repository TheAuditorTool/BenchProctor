// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00378(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = (size_t)strtoul(user_input, NULL, 10);
    if (_span > sizeof(_buf)) _span = sizeof(_buf);
    memcpy(_out, _buf, _span);
    printf("%.*s\n", (int)_span, _out);
}
