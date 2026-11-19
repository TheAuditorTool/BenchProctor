// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <libgen.h>

void benchmark_test_00105(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    char _bn_copy[512];
    snprintf(_bn_copy, sizeof(_bn_copy), "%s", user_input);
    const char *safe = basename(_bn_copy);
    FILE *_f = fopen(safe, "w");
    if (_f) fclose(_f);
}
