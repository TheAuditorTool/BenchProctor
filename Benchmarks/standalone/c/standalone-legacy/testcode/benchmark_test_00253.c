// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_payload { const char *value; };

void benchmark_test_00253(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    char *_dst = malloc(16);
    if (_dst == NULL) return;
    size_t _n = strlen(data);
    if (_n > 15) _n = 15;
    memcpy(_dst, data, _n);
    _dst[_n] = '\0';
    printf("%s\n", _dst);
    free(_dst);
}
