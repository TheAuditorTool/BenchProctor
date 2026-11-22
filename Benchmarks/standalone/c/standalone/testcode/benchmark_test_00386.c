// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00386(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    const char *_sep = strstr(data, "://");
    if (_sep != NULL) putchar(_sep[3]);
    putchar('\n');
}
