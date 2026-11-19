// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_payload { const char *value; };

void benchmark_test_01113(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    int _vals[8];
    int _idx = atoi(data) & 7;
    printf("v=%d\n", _vals[_idx]);
}
