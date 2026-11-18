// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00434(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    char _path[512];
    snprintf(_path, sizeof(_path), "/var/app/data/%s", data);
    FILE *_f = fopen(_path, "r");
    if (_f) fclose(_f);
}
