// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00539(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char *_dst = malloc(16);
    if (_dst) { strcpy(_dst, user_input); printf("%s\n", _dst); free(_dst); }
}
