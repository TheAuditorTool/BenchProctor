// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00403(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    char *_dst = malloc(32);
    if (_dst == NULL) return;
    sprintf(_dst, "user=%s", data);
    puts(_dst);
    free(_dst);
}
