// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00392(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char *_p = malloc(strlen(user_input) + 1);
    if (_p == NULL) return;
    strcpy(_p, user_input);
    free(_p);
    _p = NULL;
    if (_p) printf("%s\n", _p);
}
