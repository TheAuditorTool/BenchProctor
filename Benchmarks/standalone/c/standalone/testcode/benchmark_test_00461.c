// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00461(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    const size_t _rec_size = 64;
    long _count = strtol(data, NULL, 10);
    if (_count <= 0 || _count > 65536) return;
    size_t _bytes = (size_t)_count * _rec_size;
    char *_recs = malloc(_bytes);
    if (_recs) free(_recs);
}
