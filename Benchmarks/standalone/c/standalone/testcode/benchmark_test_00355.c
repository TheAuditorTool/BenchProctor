// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00355(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    for (char *_r = data; *_r; ++_r) if (*_r == '\n') *_r = ' ';
    const int _rec_size = 64;
    int _count = atoi(data);
    int _bytes = _count * _rec_size;
    char *_recs = malloc((size_t)_bytes);
    if (_recs) free(_recs);
}
