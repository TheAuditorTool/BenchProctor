// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00266(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    char *_p = malloc(strlen(data) + 1);
    if (_p == NULL) return;
    strcpy(_p, data);
    free(_p);
    printf("%s\n", _p);
}
