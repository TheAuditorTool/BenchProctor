// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00205(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    char *_dst = malloc(32);
    if (_dst == NULL) return;
    snprintf(_dst, 32, "user=%s", data);
    puts(_dst);
    free(_dst);
}
