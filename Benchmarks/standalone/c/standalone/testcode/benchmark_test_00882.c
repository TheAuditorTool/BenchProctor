// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00882(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    char _buf[16] = "fixedcontent12";
    size_t _span = (size_t)strtoul(data, NULL, 10);
    fwrite(_buf, 1, _span, stdout);
    putchar('\n');
}
