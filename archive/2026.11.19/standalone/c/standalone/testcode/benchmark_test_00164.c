// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00164(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    size_t _li = 0;
    for (; user_input[_li] != '\0' && _li < sizeof(data) - 1; ++_li) data[_li] = user_input[_li];
    data[_li] = '\0';
    long _req = strtol(data, NULL, 10);
    if (_req < 0 || _req > 2147483646L) return;
    long _alloc = _req + 1;
    char *_buf = malloc((size_t)_alloc);
    if (_buf) free(_buf);
}
