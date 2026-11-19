// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_payload { const char *value; };

void benchmark_test_01065(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    char *_parts[2];
    _parts[0] = malloc(strlen(data) + 1);
    if (_parts[0] == NULL) return;
    strcpy(_parts[0], data);
    _parts[1] = _parts[0];
    printf("%s\n", _parts[0]);
    for (int _k = 0; _k < 2; _k++) free(_parts[_k]);
}
