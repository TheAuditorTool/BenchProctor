// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_payload { const char *value; };

void benchmark_test_00436(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    const int _rec_size = 64;
    int _count = atoi(data);
    int _bytes = _count * _rec_size;
    char *_recs = malloc((size_t)_bytes);
    if (_recs) free(_recs);
}
