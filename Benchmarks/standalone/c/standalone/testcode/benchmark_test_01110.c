// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_01110(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    size_t _li = 0;
    for (; user_input[_li] != '\0' && _li < sizeof(data) - 1; ++_li) data[_li] = user_input[_li];
    data[_li] = '\0';
    const int _rec_size = 64;
    int _count = atoi(data);
    int _bytes = _count * _rec_size;
    char *_recs = malloc((size_t)_bytes);
    if (_recs) free(_recs);
}
