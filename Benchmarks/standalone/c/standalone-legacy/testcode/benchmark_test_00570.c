// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00570(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    size_t _n = strlen(data);
    int _mode;
    if (_n > 64) _mode = 2;
    else if (_n > 0) _mode = 1;
    printf("%d\n", _mode);
}
