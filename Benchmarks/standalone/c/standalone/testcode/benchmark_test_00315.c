// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00315(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    switch (user_input[0]) {
        case '\0':
            data[0] = '\0';
            break;
        default:
            snprintf(data, sizeof(data), "%s", user_input);
            break;
    }
    const int _rec_size = 64;
    int _count = atoi(data);
    int _bytes = _count * _rec_size;
    char *_recs = malloc((size_t)_bytes);
    if (_recs) free(_recs);
}
