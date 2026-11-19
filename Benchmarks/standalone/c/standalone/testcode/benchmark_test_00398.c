// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00398(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    for (char *_r = data; *_r; ++_r) if (*_r == '\n') *_r = ' ';
    char *_dst = malloc(16);
    if (_dst == NULL) return;
    size_t _n = strlen(data);
    if (_n > 15) _n = 15;
    memcpy(_dst, data, _n);
    _dst[_n] = '\0';
    printf("%s\n", _dst);
    free(_dst);
}
