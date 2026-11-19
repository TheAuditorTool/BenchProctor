// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00745(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    char *_dst = malloc(16);
    if (_dst == NULL) return;
    size_t _n = strlen(user_input);
    memcpy(_dst, user_input, _n + 1);
    printf("%s\n", _dst);
    free(_dst);
}
