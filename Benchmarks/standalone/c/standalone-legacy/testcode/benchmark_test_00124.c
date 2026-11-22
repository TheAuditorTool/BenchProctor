// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00124(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    const char *_sep = strstr(data, "://");
    if (_sep != NULL) putchar(_sep[3]);
    putchar('\n');
}
