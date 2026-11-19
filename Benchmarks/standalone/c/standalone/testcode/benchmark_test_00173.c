// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_payload { const char *value; };

void benchmark_test_00173(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    char *_p = malloc(16);
    if (_p == NULL) return;
    strcpy(_p, "pending");
    printf("%s\n", _p);
    free(_p);
    _p = malloc(strlen(data) + 1);
    if (_p == NULL) return;
    strcpy(_p, data);
    printf("%s\n", _p);
    free(_p);
}
