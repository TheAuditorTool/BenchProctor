// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00248(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    char *_p = malloc(strlen(data) + 1);
    if (_p == NULL) return;
    strcpy(_p, data);
    free(_p);
    char _first = _p[0];
    printf("%c\n", _first);
}
