// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00341(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    int _req = atoi(data);
    int _alloc = _req + 1;
    char *_buf = malloc((size_t)_alloc);
    if (_buf) free(_buf);
}
