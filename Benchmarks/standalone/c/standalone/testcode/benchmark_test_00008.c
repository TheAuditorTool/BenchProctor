// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_payload { const char *value; };

void benchmark_test_00008(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    int _req = atoi(data);
    int _alloc = _req + 1;
    char *_buf = malloc((size_t)_alloc);
    if (_buf) free(_buf);
}
