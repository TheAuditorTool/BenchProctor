// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00526(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *_sep = strstr(user_input, "://");
    if (_sep != NULL) putchar(_sep[3]);
    putchar('\n');
}
