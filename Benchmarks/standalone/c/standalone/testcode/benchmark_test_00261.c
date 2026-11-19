// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00261(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    size_t _n = strlen(user_input);
    char *_p = malloc(_n + 1);
    if (_p == NULL) return;
    memcpy(_p, user_input, _n + 1);
    printf("%s\n", _p);
    free(_p);
    memset(_p, 0, _n + 1);
}
