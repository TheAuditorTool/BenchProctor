// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00096(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    char _dst[16];
    if (strlen(data) < sizeof(_dst)) strcpy(_dst, data);
    else _dst[0] = '\0';
    printf("%s\n", _dst);
}
