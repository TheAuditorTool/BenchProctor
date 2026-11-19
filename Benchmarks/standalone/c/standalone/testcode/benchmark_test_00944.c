// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00944(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    char *_p = malloc(strlen(data) + 1);
    if (_p == NULL) return;
    strcpy(_p, data);
    char _first = _p[0];
    free(_p);
    printf("%c\n", _first);
}
