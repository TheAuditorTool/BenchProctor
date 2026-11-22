// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00385(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    size_t _n = strlen(data);
    char *_p = malloc(_n + 1);
    if (_p == NULL) return;
    memcpy(_p, data, _n + 1);
    printf("%s\n", _p);
    memset(_p, 0, _n + 1);
    free(_p);
}
